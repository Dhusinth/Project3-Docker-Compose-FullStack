from flask import Flask, jsonify
import mysql.connector
import redis
import os

app = Flask(__name__)

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")

REDIS_HOST = os.environ.get("REDIS_HOST")


@app.route('/health')
def health():

    return jsonify({
        "status": "Backend Healthy"
    })


@app.route('/db-check')
def db_check():

    try:

        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        conn.close()

        return jsonify({
            "database": "MySQL Connected"
        })

    except Exception as e:

        return jsonify({
            "database": "Connection Failed",
            "error": str(e)
        }), 500


@app.route('/redis-check')
def redis_check():

    try:

        r = redis.Redis(host=REDIS_HOST, port=6379)

        r.ping()

        return jsonify({
            "redis": "Redis Connected"
        })

    except Exception as e:

        return jsonify({
            "redis": "Connection Failed",
            "error": str(e)
        }), 500


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)