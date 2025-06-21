
# 🚗 Car Survey App

A simple yet elegant **Flask web application** to collect user input on their **favorite** and **owned cars**, storing the data in a MySQL database. The entire project is containerized using **Docker** and can be set up easily using `docker-compose` or manual Docker CLI commands.

---

## 📦 Technologies Used

- Python 3.x
- Flask 2.x
- MySQL 5.7
- Docker
- Docker Compose
- HTML/CSS frontend with background image

---

## 📸 UI Preview

![UI Preview](![image](https://github.com/user-attachments/assets/66dd0c5b-b7bb-4783-99b4-2624573bb852)

---

## 🚀 How to Run This Project

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/vardaan412/car-survey-app.git
cd car-survey-app
````

---

## 🧠 Option 1: Using Docker Compose (Recommended)

```bash
# Make sure Docker is installed and running
docker-compose up --build -d
```

Then open:
🔗 [http://localhost:5000](http://localhost:5000)

---

## ⚙️ Option 2: Manual Docker Setup (If docker-compose is not available)

### 1. Clean up old containers and images (Optional)

```bash
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images -q)
```

### 2. Create Docker Network

```bash
docker network create car-net
```

### 3. Run MySQL Container

```bash
docker run -d \
  --name mysql-container \
  --network car-net \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=car_db \
  -p 3306:3306 \
  mysql:5.7
```

### 4. Wait 20–30 seconds and then import schema

```bash
docker exec -i mysql-container \
  mysql -u root -ppassword car_db < schema.sql
```

### 5. Build Flask App Docker Image

```bash
docker build -t car-flask-app .
```

### 6. Run Flask App Container

```bash
docker run -d \
  --name flask-app \
  --network car-net \
  -p 5000:5000 \
  car-flask-app
```

Visit the app at:
🔗 [http://localhost:5000](http://localhost:5000)

---

## 🗃️ Project Structure

```
car-survey-app/
├── app.py
├── config.py
├── schema.sql
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## 🙋‍♂️ Author

**Vardaan Saxena**
🔗 [GitHub Profile](https://github.com/vardaan412)

---

