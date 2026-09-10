const CACHE_NAME = "mi-app-v1";

const archivos = [
    "/",
    "/index.html",
    "/manifest.json"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(archivos))
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(respuesta => respuesta || fetch(event.request))
    );
});
0

