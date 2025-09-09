# Django Ecommerce Project

A comprehensive ecommerce web application built with Django, demonstrating modern web development practices, database relationships, payment integration, and production deployment considerations.

## 🎯 Project Overview

This project is a full-featured ecommerce platform designed to showcase and implement various web development concepts including CRUD operations, Object-Relational Mapping (ORM), payment gateway integration, and production-ready deployment strategies. The application focuses on dairy products (Kwartha Milk) and provides a complete shopping experience from product browsing to order completion.

## 🚀 Key Learning Objectives

- **CRUD Operations**: Complete Create, Read, Update, Delete functionality for products, users, and orders
- **Database Relationships**: Implementation of complex database relationships (One-to-Many, Many-to-One, Many-to-Many)
- **Payment Integration**: Real-world payment processing using Razorpay gateway
- **Static File Management**: Handling CSS, JavaScript, and media files in both development and production
- **Template Rendering**: Django's powerful template engine with Bootstrap integration
- **Web Server Technologies**: Understanding WSGI/ASGI protocols for web server communication
- **Production Deployment**: Integration with Nginx and WhiteNoise for static file serving
- **Security Best Practices**: Environment-based configuration and secret management

## 🛠️ Technologies Used

### Backend
- **Django 4.2.3** - High-level Python web framework
- **Python 3.x** - Programming language
- **SQLite** - Development database (easily configurable for PostgreSQL/MySQL)
- **Django ORM** - Object-Relational Mapping for database operations

### Frontend
- **Bootstrap** - Responsive CSS framework
- **HTML5/CSS3** - Modern web markup and styling
- **JavaScript** - Client-side interactivity

### Payment & External Services
- **Razorpay** - Payment gateway integration
- **Django REST Framework** - API development capabilities

### Production & Deployment
- **WhiteNoise** - Static file serving for production
- **Nginx** - Web server and reverse proxy (deployment ready)
- **python-dotenv** - Environment variable management
- **WSGI/ASGI** - Web server interface protocols

## 📊 Database Schema & Relationships

### Core Models

1. **Product**
   - Product information, pricing, categories
   - Image handling with Pillow

2. **Customer Profile**
   - User profile extension
   - Address and contact information
   - **Relationship**: One-to-Many with User

3. **Cart**
   - Shopping cart functionality
   - **Relationships**: Many-to-One with User and Product

4. **Payment**
   - Razorpay payment processing
   - Payment status tracking
   - **Relationship**: One-to-Many with User

5. **Order Placement**
   - Order management and tracking
   - **Relationships**: Many-to-One with User, Customer Profile, Product, and Payment

6. **Wishlist**
   - User wishlist functionality
   - **Relationships**: Many-to-Many through User and Product

### Database Relationship Types Implemented
- **One-to-Many**: User → Orders, User → Cart Items
- **Many-to-One**: Orders → User, Cart → Product
- **Many-to-Many**: Users ↔ Products (through Cart and Wishlist)

## 🏗️ Project Structure

```
ecommerce1/
├── ecommerce/              # Main project configuration
│   ├── settings.py         # Django settings with environment variables
│   ├── urls.py            # URL routing configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── app/                    # Core ecommerce functionality
│   ├── models.py          # Database models and relationships
│   ├── views.py           # Business logic and view controllers
│   ├── urls.py            # App-specific URL patterns
│   ├── admin.py           # Django admin configuration
│   └── templates/         # HTML templates with Bootstrap
├── account/                # User authentication and management
│   ├── forms.py           # User registration and login forms
│   ├── views.py           # Authentication views
│   └── urls.py            # Authentication URL patterns
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User-uploaded files
├── req.txt                # Dependencies documentation
└── manage.py              # Django management script
```

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ritiksharmaaa/ecommerce1.git
   cd ecommerce1
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv ecommerce_env
   source ecommerce_env/bin/activate  # On Windows: ecommerce_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install Django==4.2.3 pillow python-dotenv razorpay djangorestframework
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   RAZORPAY_KEY_ID=your_razorpay_key_id
   RAZORPAY_KEY_SECRET=your_razorpay_key_secret
   EMAIL_APP_PASSWORD=your_email_app_password
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🌟 Features

### Customer Features
- **Product Browsing**: Category-wise product listing with detailed views
- **User Authentication**: Registration, login, logout functionality
- **Shopping Cart**: Add/remove products, quantity management
- **Wishlist**: Save products for later purchase
- **Order Management**: Place orders, track order status
- **Payment Processing**: Secure payment via Razorpay gateway
- **Profile Management**: Update personal and shipping information

### Admin Features
- **Product Management**: Add, edit, delete products
- **Order Tracking**: Monitor and update order status
- **User Management**: Customer profile administration
- **Payment Monitoring**: Track payment transactions

### Technical Features
- **Responsive Design**: Bootstrap-based mobile-friendly interface
- **Image Handling**: Product image upload and management
- **Email Integration**: Order confirmation and notifications
- **Search Functionality**: Product search capabilities
- **State Management**: Indian state selection for shipping

## 🔒 Security & Production Considerations

### Environment Variables
- Sensitive data (API keys, passwords) stored in `.env` file
- Production settings separated from development
- Django secret key management

### Static Files in Production
- **WhiteNoise**: Configured for serving static files in production
- **Nginx**: Ready for reverse proxy configuration
- Optimized static file collection and compression

### Deployment Ready Features
- **WSGI Configuration**: Production-ready web server interface
- **ASGI Support**: Asynchronous capabilities for scalability
- **Database Flexibility**: Easy migration from SQLite to PostgreSQL/MySQL
- **Media File Handling**: Proper configuration for user uploads

## 🎓 Learning Outcomes

This project provides hands-on experience with:

1. **Web Development Fundamentals**
   - MVC/MVT architecture pattern
   - RESTful API principles
   - Frontend-backend integration

2. **Database Design**
   - Relational database modeling
   - ORM query optimization
   - Data integrity and validation

3. **Payment Systems**
   - Third-party API integration
   - Secure transaction handling
   - Webhook processing

4. **Production Deployment**
   - Static file optimization
   - Web server configuration
   - Environment management
   - Security best practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is created for educational purposes and learning Django web development.

## 📞 Support

For questions or support, please open an issue in the GitHub repository.

---

**Note**: This project is designed as a learning platform for understanding Django development, ORM relationships, payment integration, and production deployment strategies. It demonstrates real-world ecommerce functionality while maintaining clean, educational code structure.