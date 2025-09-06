# מתוך התיקייה שבה נמצא docker-compose.yml
docker compose up --build
# או ברקע
# docker compose up -d --build

# לראות סטטוס
docker compose ps

# לראות לוגים של שירות מסוים (למשל של ה-API)
docker compose logs -f api
