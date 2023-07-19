# MonoChat

ChatGPT (Azure OpenAI Service) を利用したSlack上で動くChat bot

※ このリポジトリは参照用に切り出したもので、更新する予定は今のところありません。

※ 本Slackbotについて書いたブログは[こちら](https://tech-blog.monotaro.com/entry/2023/07/19/090000)から

## 各種手順

    # virtualenv などのセットアップを行う
    make setup

    # アプリケーションを実行する
    make run

    # サーバに ssh する
    gcloud compute ssh --project={your project name} --zone={your zone} {your instance name}

    # ファイルを転送する
    gcloud compute scp --project={your project name} --zone={your zone} {転送したいファイル} {your instance name}:{転送先パス}

## 環境

- Google Cloud Platform
  - Compute Engine
  - Secret Manager
- Python3
- Slack Bolt for Python
- Azure OpenAI Service

Compute Engine上で、SystemdのServiceで複数プロセスを立てて負荷分散している

## サーバーへのデプロイ

GitHub Actionsにて自動デプロイを実装しており、mainブランチにpush or mergeすると自動でデプロイが走る

## Slack App登録時に必要な権限

```YAML
# App manifestの一部を抜粋
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - channels:history
      - channels:read
      - chat:write
      - groups:history
      - im:history
      - mpim:history
      - reactions:read
      - commands
settings:
  event_subscriptions:
    bot_events:
      - app_mention
      - message.channels
      - message.groups
      - message.im
      - message.mpim
      - reaction_added
```

## License

This project is licensed under the
[MIT license](https://opensource.org/licenses/MIT).  See
[LICENSE](./LICENSE) for the full
license text.