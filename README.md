<div align="center">
<img width="460" src="https://raw.githubusercontent.com/fajfer/billy-h-scraper/main/assets/logo.jpg">
</div>

# Billy H. scraper #

## Czego potrzebujemy? ##

- [Dockera](https://docs.docker.com/get-docker/), lub po prostu działającego pythona na naszej maszynie
- [docker-compose](https://docs.docker.com/compose/install/)
- [Bota](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0) na Telegramie (potrzebujemy jego token)

## Uruchomienie dockera ##

### Budowanie projektu  ###

Zbudowanie projektu polega na uruchomieniu polecenia
```console
docker build --network=host -t fajfer/billy-h-scraper:latest .
```

### 'Czysty' docker ###

Skrypt można uruchomić jedną linijką, jeżeli nie zależy nam na wygodzie docker-compose

```console
docker run \
  --env WEB_URL='<url>' \
  --env GROUPS='<grupy oddzielone przecinkami>' \
  --env BOT_TOKEN='<token>' \
  --env MSG_DELAY='<int>' \
  --volume ./history:/app/history \
  fajfer/billy-h-scraper:latest
```

### Docker compose ###

Możemy też utrzymywać konfigurację w wygodnym YAMLu i postawić kontener jednym poleceniem

```console
docker-compose up -d
```

### Zbudowanie obrazu i uruchomienie kontenera za jednym zamachem

Można też zbudować obraz projektu i go uruchomić jednym poleceniem, dzięki docker-compose

```console
docker compose up -d --build
```

## Wyjaśnienie użytych zmiennych ##

### Required variable combinations ###

| Nazwa          | Przykład  |  Zastosowanie  |
|----------------|-----------|----------------|
| `WEB_URL`      | https://www.wp.pl          | Adres URL wybranego shoutboxa |
| `GROUPS`       | @wp_pl,@onet_pl            | ID grup na telegramie oddzielonych przecinkami |
| `BOT_TOKEN`    | 000000:AAAAAABBBBBBCCCCCCC | Token, jaki otrzymaliśmy od BotFathera na Telegramie |
| `MSG_DELAY`    | 60                         | Zmianna odpowiadająca liczbie sekund zanim zostanie odpytany endpoint `SHOUTBOX_URL` |
