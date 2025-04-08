# 📌 Flask Task Manager

Современное веб-приложение для управления задачами с возможностью регистрации, авторизации, создания, редактирования и удаления задач. 

Разработано на Flask с использованием Bootstrap 5 и SQLite.

---

## 🔧 Функционал

- ✅ Регистрация и вход пользователей
- ✅ Панель управления задачами (dashboard)
- ✅ CRUD (создание, просмотр, редактирование, удаление) задач
- ✅ Фильтрация задач по статусу
- ✅ Flash-сообщения (успехи, ошибки)
- ✅ Стильный и адаптивный интерфейс (Bootstrap + кастомные стили)

---

## 🖼️ Интерфейс

![screenshot](https://via.placeholder.com/800x400.png?text=Task+Manager+Preview)

---

## 🚀 Как запустить

1. **Клонировать репозиторий**

```bash
git clone https://github.com/yourusername/flask-task-manager.git
cd flask-task-manager 
```

2. **Создать и активировать виртуальное окружение**

python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

3. **Установить зависимости**

pip install -r requirements.txt


4. **Запустить приложение**

flask db init
flask db migrate -m "initial"
flask db upgrade
flask run


5. **Открыть в браузере**

http://127.0.0.1:5000/