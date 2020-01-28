# Preparations
* Create bot.env file, put variable BOT_TOKEN=... in it. BOT_TOKEN is a telegram token of the bot.

# Build leranauchi_bot docker image
```docker image build -t leranauchi_bot .```

# Run service on swarm
```docker stack deploy -c stack.yaml lera_bot```

## .. or run beta version, assuming we have proper BOT_TOKEN=.. in dev.env file
```docker stack deploy -c stack.yaml -c stack.beta.yaml lera_bot```

