
# Beadandó Feladat - DevOps

Ez a projekt egy egyszerű Python Flask alapú webalkalmazást tartalmaz, amely CI/CD pipeline segítségével automatikusan tesztelésre kerül, majd Docker image formájában feltöltődik a GitLab Container Registry-be.

## 1. Programkód lényege
Az alkalmazás (`app.py`) egy REST API végpontot biztosít a `/` útvonalon, amely HTTP GET kérésre egy JSON üzenettel válaszol (`{"message": "..."}`). Tartozik hozzá egy unit teszt (`test_app.py`), amely ellenőrzi a státuszkódot és a válasz tartalmát.

## 2. Dockerfile működése
A `Dockerfile` lépései:
1.  Python 3.9-slim alap image letöltése.
2.  Munkakönyvtár beállítása `/app`.
3.  Függőségek (`requirements.txt`) telepítése.
4.  Forráskód bemásolása.
5.  Az alkalmazás indítása a `python app.py` paranccsal.

### Lokális futtatás:
Image buildelése:
`docker build -t my-app .`

Konténer futtatása:
`docker run -p 8080:8080 my-app`

## 3. CI Pipeline
A `.gitlab-ci.yml` két fázisból áll:
1.  **Test:** Telepíti a függőségeket és lefuttatja a unit teszteket. Siker esetén létrehoz egy `test_report.txt` artifactot.
2.  **Build-Deploy:** Docker-in-Docker segítségével összeépíti az imaget, majd bejelentkezik a GitLab Registry-be és feltölti (push) az elkészült imaget.
