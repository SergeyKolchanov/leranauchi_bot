# Build leranauchi_bot docker image
```docker image build -t leranauchi_bot .```

# Run service on swarm
```docker stack deploy -c stack.yaml lera_bot```
Secret environment file bot.env is needed. It should contain BOT_TOKEN variable