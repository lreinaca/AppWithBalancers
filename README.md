Frontend service is built from ./frontend and runs in the eam_electiva network.

Backend service is built from ./backend and also connects to the same network.

Adminer service uses the official adminer image, available at http://localhost:8081, with a health check to monitor availability.

Nginx service is built from ./nginx, acts as a reverse proxy, and listens on http://localhost:8080. It depends on frontend, backend, and Adminer.

All services communicate through the custom Docker network eam_electiva.

Health checks ensure that Adminer and Nginx are running properly before handling requests.
