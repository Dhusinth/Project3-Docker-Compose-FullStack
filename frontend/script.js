async function checkServices() {

    checkBackend();
    checkDatabase();
    checkRedis();
}

async function checkBackend() {

    const backendStatus = document.getElementById("backend-status");

    try {

        const response = await fetch("/api/health");

        const data = await response.json();

        backendStatus.innerText = data.status;

    } catch (error) {

        backendStatus.innerText = "Connection Failed";
    }
}

async function checkDatabase() {

    const dbStatus = document.getElementById("db-status");

    try {

        const response = await fetch("/api/db-check");

        const data = await response.json();

        dbStatus.innerText = data.database;

    } catch (error) {

        dbStatus.innerText = "Connection Failed";
    }
}

async function checkRedis() {

    const redisStatus = document.getElementById("redis-status");

    try {

        const response = await fetch("/api/redis-check");

        const data = await response.json();

        redisStatus.innerText = data.redis;

    } catch (error) {

        redisStatus.innerText = "Connection Failed";
    }
}

checkServices();