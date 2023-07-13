import json
import os

import google.cloud.secretmanager


def get_secret() -> dict[str, str]:
    """
    シークレット情報を取得する.

    最初に環境変数からの取得を試みて,
    取得できない場合は GCP Secret Manager から取得する.
    """
    return get_secret_from_environ() or get_secret_from_secret_manager()


def get_secret_from_secret_manager() -> dict[str, str]:
    """
    GCP Secret Manager からシークレット情報を取得する.
    """

    project_id = "XXXXXXXXXXXX"  # GCPのプロジェクトID
    secret_name = "XXXXXXXXXXXX"  # Secret Managerで作成したシークレット名
    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    client = google.cloud.secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(request={"name": name})
    secret_value_json = response.payload.data.decode("UTF-8")
    return json.loads(secret_value_json)


def get_secret_from_environ() -> dict[str, str]:
    """
    環境変数からシークレット情報を取得する.

    Returns
    -------
    dict[str, str] | None:
        必要な全ての値を環境変数で取得できた場合は dict として返す.
        1 つでも取得できない値があった場合は None.
    """
    try:
        return {
            "OPENAI_API_BASE": os.environ["OPENAI_API_BASE"],
            "OPENAI_API_KEY": os.environ["OPENAI_API_KEY"],
            "SLACK_BOT_TOKEN": os.environ["SLACK_BOT_TOKEN"],
            "SLACK_API_TOKEN": os.environ["SLACK_API_TOKEN"],
            "OPENAI_DEPLOYMENT_NAME": os.environ["OPENAI_DEPLOYMENT_NAME"],
        }
    except KeyError:
        return None
