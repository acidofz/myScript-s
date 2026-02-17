RENTO - Полное Руководство для Новичков
📚 Часть 1: Основные Понятия
Что такое Frontend и Backend?
Представьте ресторан:

* Frontend (фронтенд) = зал ресторана, меню, официанты

  * То, что видит клиент

  * Красивый интерфейс

  * Кнопки, формы, картинки

* Backend (бэкенд) = кухня ресторана

  * То, что скрыто от клиента

  * Обработка данных

  * База данных

  * Логика приложения

Как они общаются?

```
┌─────────────┐         HTTP запросы        ┌─────────────┐
```

│ Frontend │ ──────────────────────────> │ Backend │
│ (браузер) │ <────────────────────────── │ (сервер) │
└─────────────┘ JSON ответы └─────────────┘
Пример:

1. Вы нажимаете кнопку "Войти" (Frontend)

2. Браузер отправляет логин и пароль на сервер (HTTP запрос)

3. Сервер проверяет данные в базе (Backend)

4. Сервер отвечает: "Успешно" или "Ошибка" (JSON ответ)

5. Браузер показывает результат (Frontend)

🔧 Часть 2: Технологии (что это и зачем)
Backend Технологии
1. Node.js - среда выполнения JavaScript
Что это?

* Обычно JavaScript работает только в браузере

* Node.js позволяет запускать JavaScript на сервере (как Python или Java)

Зачем?

* Можно писать и фронтенд, и бэкенд на одном языке

* Быстрый и популярный

2. Express - веб-фреймворк
Что это?

* Библиотека для создания веб-серверов

* Упрощает работу с HTTP запросами

Пример без Express:

```
javascript
```

// Сложно и много кода
const http = require('http');
const server = http.createServer((req, res) => {
if (req.url === '/api/users' && req.method === 'GET') {
// обработка...
  }
});
С Express:

```
javascript
```

// Просто и понятно
const express = require('express');
const app = express();
app.get('/api/users', (req, res) => {
// обработка...
});
3. SQLite - база данных
Что это?

* Место, где хранятся данные (как Excel таблица)

* Не требует установки отдельного сервера

* Всё хранится в одном файле rento.db

Структура:

```
Таблица: users
```

┌────┬──────────┬──────────┐
│ id │ username │ password │
├────┼──────────┼──────────┤
│ 1 │ john │ **** │
│ 2 │ mary │ **** │
└────┴──────────┴──────────┘
Таблица: listings
┌────┬───────────────┬───────┬──────────┐
│ id │ title │ price │ location │
├────┼───────────────┼───────┼──────────┤
│ 1 │ Modern Apt │ 450 │ Tashkent │
│ 2 │ Cozy Studio │ 300 │ Tashkent │
└────┴───────────────┴───────┴──────────┘
4. JWT (JSON Web Token) - токены авторизации
Что это?

* Зашифрованная строка, которая подтверждает личность пользователя

* Как электронный пропуск

Как работает:

```
1. Пользователь вводит логин/пароль
```

2. Сервер проверяет → создает токен
   Токен = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
3. Браузер сохраняет токен
4. При каждом запросе браузер отправляет токен
5. Сервер проверяет токен → разрешает доступ
Зачем?

* Не нужно каждый раз вводить пароль

* Безопасно (токен зашифрован)

Frontend Технологии
1. React - библиотека для UI
Что это?

* Позволяет создавать интерфейс из компонентов (как LEGO)

* Автоматически обновляет страницу при изменении данных

Пример компонента:

```
javascript
```

function Button() {
return <button>Нажми меня</button>;
}
// Использование:
<Button />
2. Vite - сборщик проекта
Что это?

* Инструмент для разработки

* Запускает локальный сервер

* Автоматически обновляет страницу при изменении кода

Команда:

```
bash
```

npm run dev # Запускает сервер на http://localhost:5173
3. React Router - навигация
Что это?

* Позволяет создавать разные страницы без перезагрузки

Пример:

```
javascript
```

<Routes>
<Route path="/" element={<HomePage />} />
<Route path="/login" element={<LoginPage />} />
</Routes>
Когда пользователь переходит на /login, показывается LoginPage.
📂 Часть 3: Структура Проекта (что где лежит)

```
RENTO.com/
```

│
├── rento-backend/ # СЕРВЕР (Backend)
│ ├── server.js # 🚀 Главный файл - запускает сервер
│ ├── database.js # 💾 Создает базу данных
│ ├── package.json # 📦 Список библиотек
│ ├── rento.db # 🗄️ Файл базы данных (создается автоматически)
│ │
│ ├── middleware/
│ │ └── auth.js # 🔐 Проверка токенов
│ │
│ └── routes/ # 🛣️ Маршруты API
│ ├── auth.js # Вход/Регистрация
│ ├── listings.js # Объявления
│ └── contracts.js # Договоры
│
└── rento-web/ # ИНТЕРФЕЙС (Frontend)
    ├── index.html # 📄 Главная HTML страница
    ├── package.json # 📦 Список библиотек
    │
    └── src/
        ├── main.jsx # 🚀 Точка входа
        ├── App.jsx # 🏠 Главный компонент
        ├── index.css # 🎨 Глобальные стили
        │
        ├── context/
        │ └── AuthContext.jsx # 👤 Управление авторизацией
        │
        ├── components/ # 🧩 Переиспользуемые части
        │ ├── Navbar.jsx
        │ ├── Hero.jsx
        │ ├── Features.jsx
        │ ├── Listings.jsx
        │ ├── Comparison.jsx
        │ └── Footer.jsx
        │
        └── pages/ # 📄 Отдельные страницы
            ├── Auth.jsx
            ├── CreateListing.jsx
            └── Contract.jsx
🔍 Часть 4: Разбор Кода (построчно)
Backend: 
server.js

```
javascript
```

// 1. Импортируем библиотеки
const express = require('express'); // Веб-фреймворк
const cors = require('cors'); // Разрешает запросы с другого порта
const db = require('./database'); // Наша база данных
// 2. Импортируем маршруты
const authRoutes = require('./routes/auth');
const listingRoutes = require('./routes/listings');
// 3. Создаем приложение
const app = express();
const PORT = 3000; // Порт сервера
// 4. Настройки
app.use(cors()); // Разрешаем запросы с localhost:5173
app.use(express.json()); // Понимаем JSON в запросах
// 5. Подключаем маршруты
app.use('/api/auth', authRoutes); // Все запросы /api/auth/* → authRoutes
app.use('/api/listings', listingRoutes); // Все запросы /api/listings/* → listingRoutes
app.use('/api/contracts', require('./routes/contracts'));
// 6. Главная страница API
app.get('/', (req, res) => {
res.send('Welcome to Rento API');
});
// 7. Запускаем сервер
app.listen(PORT, () => {
console.log(`Server running on http://localhost:${PORT}`);
});
Что происходит:

1. Когда вы запускаете node server.js

2. Сервер начинает слушать порт 3000

3. Когда приходит запрос на /api/auth/login → обрабатывает authRoutes

4. Когда приходит запрос на /api/listings → обрабатывает listingRoutes

Backend: 
routes/auth.js (Регистрация)

```
javascript
```

const express = require('express');
const bcrypt = require('bcryptjs'); // Шифрование паролей
const jwt = require('jsonwebtoken'); // Создание токенов
const db = require('../database');
const router = express.Router();
const SECRET_KEY = 'super_secret_key_rento'; // Секретный ключ для токенов
// РЕГИСТРАЦИЯ
router.post('/register', (req, res) => {
// 1. Получаем данные из запроса
const { username, password } = req.body;
// 2. Проверяем, что данные есть
if (!username || !password) {
return res.status(400).json({ error: 'Username and password required' });
  }
// 3. Шифруем пароль (чтобы не хранить в открытом виде)
const hashedPassword = bcrypt.hashSync(password, 8);
// Пример: "mypassword" → "$2a$08$Xk3j..."
// 4. Сохраняем пользователя в базу данных
db.run("INSERT INTO users (username, password) VALUES (?, ?)",
    [username, hashedPassword],
function(err) {
if (err) {
return res.status(500).json({ error: 'User already exists' });
      }
// 5. Создаем токен
const token = jwt.sign(
        { id: this.lastID, username }, // Данные в токене
SECRET_KEY, // Секретный ключ
        { expiresIn: '24h' } // Срок действия
      );
// 6. Отправляем токен клиенту
res.status(201).json({ auth: true, token });
    }
  );
});
module.exports = router;
Пошаговый пример:

1. Пользователь вводит: username: "john", password: "123456"

2. Сервер шифрует пароль: "123456" → "$2a$08$Xk3j..."

3. Сохраняет в БД: id: 1, username: "john", password: "$2a$08$Xk3j..."

4. Создает токен: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

5. Отправляет клиенту: { auth: true, token: "eyJ..." }

Backend: 
middleware/auth.js (Проверка токена)

```
javascript
```

const jwt = require('jsonwebtoken');
const SECRET_KEY = 'super_secret_key_rento';
const verifyToken = (req, res, next) => {
// 1. Получаем токен из заголовка запроса
const token = req.headers['authorization'];
// 2. Проверяем, что токен есть
if (!token) {
return res.status(403).json({ error: 'No token provided' });
  }
// 3. Убираем "Bearer " если есть
const tokenString = token.startsWith('Bearer ')
? token.slice(7) // "Bearer abc123" → "abc123"
: token;
// 4. Проверяем токен
jwt.verify(tokenString, SECRET_KEY, (err, decoded) => {
if (err) {
return res.status(500).json({ error: 'Invalid token' });
    }
// 5. Сохраняем ID пользователя из токена
req.userId = decoded.id;
// 6. Разрешаем продолжить
next();
  });
};
module.exports = verifyToken;
Как используется:

```
javascript
```

// В routes/listings.js
router.post('/', verifyToken, (req, res) => {
// verifyToken выполняется ПЕРВЫМ
// Если токен валидный → выполняется эта функция
// req.userId уже доступен
const userId = req.userId; // ID пользователя из токена
// Создаем объявление...
});
Frontend: 
App.jsx (Главный компонент)

```
javascript
```

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
// Импортируем компоненты
import Navbar from './components/Navbar';
import Hero from './components/Hero';
// ... другие компоненты
// Импортируем страницы
import Auth from './pages/Auth';
import CreateListing from './pages/CreateListing';
import Contract from './pages/Contract';
// Главная страница
const Home = () => (
<>
<Navbar />
<Hero />
<Features />
<Listings />
<Comparison />
<Footer />
</>
);
// Маршруты
const AppRoutes = () => {
return (
<Routes>
<Route path="/" element={<Home />} />
<Route path="/auth" element={<Auth />} />
<Route path="/create-listing" element={<CreateListing />} />
<Route path="/contract/:listingId" element={<Contract />} />
</Routes>
  );
};
// Главный компонент
function App() {
return (
<Router>
<AuthProvider>
<AppRoutes />
</AuthProvider>
</Router>
  );
}
export default App;
Что происходит:

1. <Router> - включает навигацию

2. <AuthProvider> - оборачивает всё приложение (теперь все компоненты могут проверить: залогинен ли пользователь)

3. <Routes> - определяет, какая страница показывается по какому URL

Пример:

* Пользователь открывает http://localhost:5173/ → показывается <Home />

* Пользователь переходит на /auth → показывается <Auth />

* Пользователь переходит на /contract/5 → показывается <Contract /> (listingId = 5)

Frontend: 
AuthContext.jsx (Управление авторизацией)

```
javascript
```

import React, { createContext, useState, useEffect, useContext } from 'react';
// 1. Создаем контекст
const AuthContext = createContext(null);
// 2. Провайдер (оборачивает всё приложение)
export const AuthProvider = ({ children }) => {
const [user, setUser] = useState(null); // Данные пользователя
const [token, setToken] = useState(localStorage.getItem('token')); // Токен
// 3. При загрузке проверяем токен
useEffect(() => {
if (token) {
try {
// Декодируем токен (получаем данные пользователя)
const payload = JSON.parse(atob(token.split('.')[1]));
setUser({ username: payload.username, id: payload.id });
      } catch (e) {
logout(); // Если токен невалидный → выходим
      }
    }
  }, [token]);
// 4. Функция входа
const login = (token) => {
localStorage.setItem('token', token); // Сохраняем в браузере
setToken(token);
  };
// 5. Функция выхода
const logout = () => {
localStorage.removeItem('token');
setToken(null);
setUser(null);
  };
// 6. Предоставляем данные всем компонентам
return (
<AuthContext.Provider value={{ user, token, login, logout }}>
{children}
</AuthContext.Provider>
  );
};
// 7. Хук для использования в компонентах
export const useAuth = () => useContext(AuthContext);
Как использовать в компонентах:

```
javascript
```

import { useAuth } from '../context/AuthContext';
function MyComponent() {
const { user, login, logout } = useAuth();
if (user) {
return <div>Привет, {user.username}!</div>;
  } else {
return <div>Вы не вошли</div>;
  }
}
Frontend: 
pages/Auth.jsx (Страница входа)

```
javascript
```

import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
const Auth = () => {
// 1. Состояния
const [isLogin, setIsLogin] = useState(true); // Вход или регистрация?
const [formData, setFormData] = useState({ username: '', password: '' });
const [error, setError] = useState('');
const { login } = useAuth();
const navigate = useNavigate();
// 2. Обработка отправки формы
const handleSubmit = async (e) => {
e.preventDefault(); // Отменяем перезагрузку страницы
setError('');
// 3. Определяем URL
const endpoint = isLogin ? '/api/auth/login' : '/api/auth/register';
try {
// 4. Отправляем запрос на сервер
const res = await fetch(`http://localhost:3000${endpoint}`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(formData) // { username: "john", password: "123" }
      });
// 5. Получаем ответ
const data = await res.json();
if (!res.ok) throw new Error(data.error);
// 6. Если успешно → сохраняем токен и переходим на главную
if (data.token) {
login(data.token);
navigate('/');
      }
    } catch (err) {
setError(err.message); // Показываем ошибку
    }
  };
// 7. Форма
return (
<div>
<form onSubmit={handleSubmit}>
<input
type="text"
placeholder="Username"
value={formData.username}
onChange={e => setFormData({...formData, username: e.target.value})}
/>
<input
type="password"
placeholder="Password"
value={formData.password}
onChange={e => setFormData({...formData, password: e.target.value})}
/>
<button type="submit">
{isLogin ? 'Login' : 'Register'}
</button>
</form>
<button onClick={() => setIsLogin(!isLogin)}>
{isLogin ? 'Sign Up' : 'Login'}
</button>
</div>
  );
};
Пошаговый пример:

1. Пользователь вводит: username: "john", password: "123456"

2. Нажимает "Login"

3. Отправляется запрос: POST http://localhost:3000/api/auth/login

4. Сервер проверяет → возвращает токен: { auth: true, token: "eyJ..." }

5. login(data.token) → токен сохраняется в localStorage

6. navigate('/') → переход на главную страницу

7. Navbar теперь показывает "Hi, john!"

🔄 Часть 5: Полный Цикл Запроса (детально)
Пример: Создание объявления
Шаг 1: Пользователь заполняет форму

```
Компонент: CreateListing.jsx
```

┌─────────────────────────────┐
│ Title: Modern Apartment │
│ Price: 450 │
│ Location: Tashkent │
│ Rooms: 2 │
│ [Publish Listing] │
└─────────────────────────────┘
Шаг 2: Нажатие кнопки

```
javascript
```

const handleSubmit = async (e) => {
e.preventDefault();
// Отправляем запрос
const res = await fetch('http://localhost:3000/api/listings', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
'Authorization': `Bearer ${token}` // ← ТОКЕН!
    },
body: JSON.stringify(formData)
  });
};
Шаг 3: Запрос летит на сервер

```
HTTP POST http://localhost:3000/api/listings
```

Headers:
  Content-Type: application/json
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Body:
{
  "title": "Modern Apartment",
  "price": 450,
  "location": "Tashkent",
  "rooms": 2,
  "image": "https://...",
  "description": "Beautiful apartment"
}
Шаг 4: Сервер получает запрос

```
javascript
```

// routes/listings.js
router.post('/', verifyToken, (req, res) => {
// 1. verifyToken проверяет токен
// - Декодирует токен
// - Получает userId = 1
// - Сохраняет в req.userId
// 2. Получаем данные
const { title, price, location, rooms, image, description } = req.body;
const userId = req.userId; // = 1
// 3. Сохраняем в базу данных
db.run(
"INSERT INTO listings (title, price, location, rooms, image, description, userId) VALUES (?, ?, ?, ?, ?, ?, ?)",
    [title, price, location, rooms, image, description, userId],
function(err) {
if (err) return res.status(500).json({ error: err.message });
// 4. Отправляем ответ
res.status(201).json({
id: this.lastID, // ID нового объявления
message: "Listing created"
      });
    }
  );
});
Шаг 5: База данных обновляется

```
Таблица: listings
```

┌────┬───────────────────┬───────┬──────────┬───────┬────────┐
│ id │ title │ price │ location │ rooms │ userId │
├────┼───────────────────┼───────┼──────────┼───────┼────────┤
│ 1 │ Cozy Studio │ 300 │ Tashkent │ 1 │ 2 │
│ 2 │ Modern Apartment │ 450 │ Tashkent │ 2 │ 1 │ ← НОВОЕ!
└────┴───────────────────┴───────┴──────────┴───────┴────────┘
Шаг 6: Ответ возвращается клиенту

```
HTTP 201 Created
```

{
  "id": 2,
  "message": "Listing created"
}
Шаг 7: Frontend обрабатывает ответ

```
javascript
```

if (res.ok) {
navigate('/'); // Переход на главную страницу
}
Шаг 8: На главной странице появляется новое объявление

```
javascript
```

// components/Listings.jsx
useEffect(() => {
fetch('http://localhost:3000/api/listings')
.then(res => res.json())
.then(data => setListings(data)); // Обновляем список
}, []);
🎯 Часть 6: Частые Вопросы Новичков
Q1: Почему нужно запускать два сервера?
A: Потому что это два разных приложения:

* Backend (порт 3000) - обрабатывает данные

* Frontend (порт 5173) - показывает интерфейс

В продакшене (на реальном сайте) фронтенд собирается в статические файлы и размещается на том же сервере.
Q2: Что такое npm install?
A: Это команда для установки библиотек (зависимостей).
Аналогия: Вы покупаете мебель (библиотеки), чтобы обставить квартиру (проект).

```
bash
```

npm install express # Устанавливает Express
Все библиотеки перечислены в 
package.json:
 

```
json
```

{
"dependencies": {
"express": "^4.18.2",
"sqlite3": "^5.1.6"
}
}
Q3: Что такое async/await?
A: Способ работы с асинхронными операциями (которые занимают время).
Без async/await:

```
javascript
```

fetch('http://localhost:3000/api/listings')
.then(res => res.json())
.then(data => console.log(data))
.catch(err => console.error(err));
С async/await (проще читать):

```
javascript
```

async function getListings() {
try {
const res = await fetch('http://localhost:3000/api/listings');
const data = await res.json();
console.log(data);
  } catch (err) {
console.error(err);
  }
}
await = "подожди, пока операция завершится"
Q4: Что такое useState и useEffect?
A: Это React хуки (специальные функции).
useState - создает переменную, которая может меняться:

```
javascript
```

const [count, setCount] = useState(0); // count = 0
setCount(5); // count = 5
setCount(count + 1); // count = 6
Когда count меняется → React автоматически обновляет интерфейс.
useEffect - выполняет код при загрузке компонента:

```
javascript
```

useEffect(() => {
console.log('Компонент загрузился!');
// Загружаем данные с сервера
fetch('http://localhost:3000/api/listings')
.then(res => res.json())
.then(data => setListings(data));
}, []); // [] = выполнить один раз при загрузке
Q5: Что такое props и children?
A: Способ передачи данных между компонентами.
Props (свойства):

```
javascript
```

// Родительский компонент
<Button text="Нажми меня" color="blue" />
// Компонент Button
function Button(props) {
return <button style={{ color: props.color }}>
{props.text}
</button>;
}
Children (дочерние элементы):

```
javascript
```

// Родительский компонент
<Card>
<h1>Заголовок</h1>
<p>Текст</p>
</Card>
// Компонент Card
function Card({ children }) {
return <div className="card">
{children} {/* Здесь будет <h1> и <p> */}
</div>;
}
Q6: Как работает localStorage?
A: Это хранилище в браузере (как cookie, но проще).

```
javascript
```

// Сохранить
localStorage.setItem('token', 'abc123');
// Получить
const token = localStorage.getItem('token'); // 'abc123'
// Удалить
localStorage.removeItem('token');
Важно: Данные сохраняются даже после закрытия браузера!
🚀 Часть 7: Как Запустить Проект (пошагово)
Шаг 1: Открыть терминал
Linux/Mac:

* Нажмите Ctrl + Alt + T

Windows:

* Нажмите Win + R → введите cmd → Enter

Шаг 2: Перейти в папку backend

```
bash
```

cd /home/fuji/RENTO.com/rento-backend
Что это значит:

* cd = change directory (сменить папку)

* Теперь вы находитесь в папке rento-backend

Шаг 3: Установить зависимости (если еще не установлены)

```
bash
```

npm install
Что происходит:

* npm читает 
  package.json

* Скачивает все библиотеки (express, sqlite3, и т.д.)

* Сохраняет их в папку node_modules/

Время: ~1-2 минуты
Шаг 4: Запустить backend

```
bash
```

node server.js
Вы увидите:

```
Seeding database...
```

Database seeded!
Server running on http://localhost:3000
Важно: Не закрывайте этот терминал!
Шаг 5: Открыть ВТОРОЙ терминал
Шаг 6: Перейти в папку frontend

```
bash
```

cd /home/fuji/RENTO.com/rento-web
Шаг 7: Установить зависимости

```
bash
```

npm install
Шаг 8: Запустить frontend

```
bash
```

npm run dev
Вы увидите:

```
VITE v5.3.1  ready in 500 ms
```

  ➜ Local: http://localhost:5173/
  ➜ Network: use --host to expose
Шаг 9: Открыть браузер
Перейдите на: http://localhost:5173
Готово! 🎉
🔧 Часть 8: Как Изменить Код
Пример 1: Добавить новое поле в объявление
Задача: Добавить поле "Площадь" (area)
Шаг 1: Обновить базу данных
Файл: 
rento-backend/database.js
 

```
javascript
```

db.run(`CREATE TABLE IF NOT EXISTS listings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  price INTEGER,
  location TEXT,
  rooms INTEGER,
  area INTEGER, // ← ДОБАВИТЬ
  image TEXT,
  description TEXT,
  userId INTEGER,
  FOREIGN KEY(userId) REFERENCES users(id)
)`);
Шаг 2: Обновить API
Файл: 
rento-backend/routes/listings.js
 

```
javascript
```

router.post('/', verifyToken, (req, res) => {
const { title, price, location, rooms, area, image, description } = req.body;
// ↑ ДОБАВИТЬ
db.run(
"INSERT INTO listings (title, price, location, rooms, area, image, description, userId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
// ↑ ДОБАВИТЬ
    [title, price, location, rooms, area, image, description, req.userId],
// ↑ ДОБАВИТЬ
// ...
  );
});
Шаг 3: Обновить форму
Файл: 
rento-web/src/pages/CreateListing.jsx
 

```
javascript
```

const [formData, setFormData] = useState({
title: '',
price: '',
location: '',
rooms: '',
area: '', // ← ДОБАВИТЬ
image: '',
description: ''
});
// В форме:
<input
type="number"
placeholder="Area (m²)"
value={formData.area}
onChange={e => setFormData({...formData, area: e.target.value})}
/>
Шаг 4: Показать в списке
Файл: 
rento-web/src/components/Listings.jsx
 

```
javascript
```

<div>
<span>📍 {listing.location}</span>
<span>🛏️ {listing.rooms} rooms</span>
<span>📐 {listing.area} m²</span> {/* ← ДОБАВИТЬ */}
</div>
Шаг 5: Перезапустить

1. Остановить backend (Ctrl + C)

2. Удалить старую базу: rm rento.db

3. Запустить снова: node server.js

Frontend обновится автоматически (благодаря Vite).
📚 Часть 9: Полезные Ресурсы
Документация

* React: https://react.dev/

* Express: https://expressjs.com/

* SQLite: https://www.sqlite.org/

Обучение

* JavaScript: https://javascript.info/

* React для начинающих: https://react.dev/learn

* Node.js: https://nodejs.org/en/learn

Инструменты

* VS Code - редактор кода

* Postman - тестирование API

* DB Browser for SQLite - просмотр базы данных

🎓 Заключение
Поздравляю! Теперь вы понимаете:

* ✅ Как работает fullstack приложение

* ✅ Что такое frontend и backend

* ✅ Как общаются клиент и сервер

* ✅ Как работает авторизация

* ✅ Как изменять код

Следующие шаги:

1. Попробуйте запустить проект

2. Зарегистрируйтесь и создайте объявление

3. Попробуйте изменить что-то в коде

4. Изучите документацию React и Express

Удачи в изучении программирования! 🚀

создай мне сайт в котором помести выше стояшие слова