# Deploying Your Golf App to `golf.botric.co.uk` with SSL (GoDaddy Domain) Using Traefik

This guide explains how to make your Flask golf app publicly available at [https://golf.botric.co.uk](https://golf.botric.co.uk) using your GoDaddy domain, with HTTPS and your app running locally on port **8585**, using **Traefik** as the reverse proxy and automatic SSL provider.

---

## 1. **Prerequisites**

- Your app is running on a server (e.g., Fedora) at port **8585** (using Podman or Docker).
- You have access to your GoDaddy account for DNS management.
- You have root or sudo access to your server.
- You want to use **Traefik** as a reverse proxy to handle SSL and forward requests to your app.

---

## 2. **Set Up DNS on GoDaddy**

1. **Log in** to your GoDaddy account.
2. Go to **My Products** > **Domains** > **botric.co.uk** > **DNS**.
3. **Add a CNAME or A record**:
   - **CNAME** (if you have a static public hostname):  
     - Name: `golf`
     - Type: `CNAME`
     - Value: your server's public DNS name (e.g., `yourserver.example.com`)
   - **A Record** (if you have a static public IP):  
     - Name: `golf`
     - Type: `A`
     - Value: your server's public IP address

4. **Save** changes.  
   _DNS changes may take up to 1 hour to propagate._

---

## 3. **Set Up Traefik with Docker/Podman**

### Example `docker-compose.yml` (works similarly with Podman Compose):

```yaml
version: "3.8"

services:
  traefik:
    image: traefik:v2.11
    command:
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--providers.docker=true"
      - "--certificatesresolvers.letsencrypt.acme.tlschallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.email=your-email@example.com"
      - "--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json"
      - "--log.level=INFO"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./letsencrypt:/letsencrypt"
    restart: always

  golf-app:
    image: your-golf-app-image
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.golf.rule=Host(`golf.botric.co.uk`)"
      - "traefik.http.routers.golf.entrypoints=websecure"
      - "traefik.http.routers.golf.tls.certresolver=letsencrypt"
      - "traefik.http.services.golf.loadbalancer.server.port=8585"
    expose:
      - "8585"
    restart: always
```

- Replace `your-golf-app-image` with your actual image name.
- Update the email in the Traefik service for Let's Encrypt notifications.

---

## 4. **Start Traefik and Your App**

```sh
docker-compose up -d
# or
podman-compose up -d
```

---

## 5. **Firewall Configuration**

Allow HTTP and HTTPS:

```sh
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload
```

---

## 6. **Test Your Site**

- Visit [https://golf.botric.co.uk](https://golf.botric.co.uk)
- You should see your golf app, with a valid SSL certificate.

---

## 7. **Renewal**

Traefik will automatically renew your Let's Encrypt SSL certificate.

---

## 8. **Troubleshooting**

- **DNS not resolving?** Wait for propagation or check your GoDaddy DNS settings.
- **SSL errors?** Check Traefik logs (`docker logs traefik`).
- **App not loading?** Ensure your app is running and accessible on port 8585 inside the container.

---

## 9. **Summary**

- DNS: `golf.botric.co.uk` → your server
- Traefik: HTTPS reverse proxy → `golf-app:8585`
- SSL: Free via Traefik/Let's Encrypt
- App: Still runs on port 8585, public access via HTTPS

---

**Tip:**  
If you update your app, just restart your container.  
Traefik and SSL will keep working.

---