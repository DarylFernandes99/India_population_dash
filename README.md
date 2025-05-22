# India Population Dashboard

A comprehensive interactive web application built with **Dash and Plotly** to visualize India's population data from the 2011 Census. This dashboard provides insights into district-wise and state-wise population distribution with interactive charts and data tables.

![Python](https://img.shields.io/badge/Python-3.7.9-blue)
![Dash](https://img.shields.io/badge/Dash-1.21.0-green)
![Plotly](https://img.shields.io/badge/Plotly-4.14.1-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Data Source](#data-source)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## ✨ Features

### 📊 Interactive Data Visualization
- **Interactive Data Table**: Sortable, filterable table displaying state-wise population data
- **State-wise Pie Chart**: Visual representation of population distribution across selected states
- **District-wise Bar Chart**: Comparative analysis of male and female population by districts
- **Multi-row Selection**: Select multiple states to compare population data
- **Real-time Updates**: Charts update dynamically based on table selections

### 🔧 Technical Features
- **Responsive Design**: Mobile-friendly interface with CSS Grid layout
- **Data Filtering**: Native filtering capabilities on all columns
- **Pagination**: Efficient data handling with 10 rows per page
- **Cross-filtering**: Interactive selection between table and charts
- **Custom Styling**: Professional CSS styling for enhanced user experience

## 📸 Screenshots

The dashboard includes three main components:
1. **Data Table**: Displays Population, Male, and Female counts by state
2. **Pie Chart**: Shows proportional population distribution
3. **Bar Chart**: Compares male vs female population by districts

## 📊 Data Source

- **Dataset**: India Districts Census 2011
- **File**: `india-districts-census-2011.csv`
- **Coverage**: All districts across India
- **Metrics**: Total Population, Male Population, Female Population
- **Granularity**: District-level data aggregated by states

### Data Processing
The application processes the raw district-level data by:
- Grouping districts by state names
- Aggregating population counts (Total, Male, Female)
- Providing both state-level overview and district-level details

## 🛠️ Technology Stack

### Backend
- **Python 3.7.9**: Core programming language
- **Dash 1.21.0**: Web application framework
- **Plotly 4.14.1**: Interactive visualization library
- **Pandas 1.1.3**: Data manipulation and analysis

### Frontend
- **Dash HTML Components**: UI structure
- **Dash Core Components**: Interactive components
- **Dash DataTable**: Advanced table functionality
- **Custom CSS**: Responsive grid layout and styling

### Deployment
- **Heroku**: Cloud platform for deployment
- **Gunicorn**: WSGI HTTP Server
- **Git**: Version control

## 🚀 Installation

### Prerequisites
- Python 3.7.9 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Option 1: Windows Quick Setup (Recommended)

1. **Run the automated setup**:
   ```bash
   createVirtualEnv.bat
   ```
   This script will:
   - Install virtualenv
   - Create a virtual environment
   - Install all dependencies from requirements.txt

2. **Start the application**:
   ```bash
   executeDash.bat
   ```

### Option 2: Manual Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   
   **Windows**:
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

## 🖥️ Usage

### Running the Application

1. **Start the server**:
   - Windows: Run `executeDash.bat`
   - Others: `python app.py`

2. **Access the dashboard**:
   - Open your browser
   - Navigate to `http://127.0.0.1:8050/`

### Interacting with the Dashboard

1. **Data Table Navigation**:
   - Use pagination controls to browse through states
   - Click column headers to sort data
   - Use filter boxes to search specific states

2. **Chart Interaction**:
   - Select rows in the data table to update charts
   - Multiple row selection shows comparative data
   - Charts automatically update with new selections

3. **Data Analysis**:
   - Compare population across different states
   - Analyze male-female ratio by districts
   - Identify population hotspots and patterns

## 📁 Project Structure

```
India_population_dash/
├── app.py                              # Main application file
├── requirements.txt                    # Python dependencies
├── runtime.txt                        # Python version for Heroku
├── Procfile                           # Heroku deployment configuration
├── LICENSE                            # MIT License
├── README.md                          # Project documentation
├── createVirtualEnv.bat               # Windows setup script
├── executeDash.bat                    # Windows execution script
├── data/
│   └── india-districts-census-2011.csv # Census data file
├── assets/
│   └── app.css                        # Custom CSS styling
└── .git/                              # Git repository files
```

### Key Files Description

- **`app.py`**: Core application with Dash layout and callbacks
- **`data/india-districts-census-2011.csv`**: Census dataset
- **`assets/app.css`**: Responsive CSS grid layout
- **`requirements.txt`**: All Python package dependencies
- **`Procfile`**: Heroku deployment configuration
- **`*.bat`**: Windows automation scripts

## 🔧 Configuration

### Environment Variables
The application uses default Dash settings but can be configured with:
- `PORT`: Server port (default: 8050)
- `DEBUG`: Debug mode (default: True for development)

### CSS Customization
Modify `assets/app.css` to change:
- Grid layout and responsiveness
- Color schemes and typography
- Component spacing and styling

## 🚀 Deployment

### Heroku Deployment

The application is configured for Heroku deployment with:

1. **Procfile**: Gunicorn WSGI server configuration
2. **runtime.txt**: Python version specification
3. **requirements.txt**: All dependencies listed

### Deploy to Heroku:

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Deploy
git push heroku main

# Scale web dyno
heroku ps:scale web=1
```

### Alternative Deployment Options
- **AWS EC2**: Deploy using Docker containers
- **Google Cloud Platform**: Use Cloud Run or App Engine
- **Local Server**: Run with Gunicorn for production

## 📈 Performance Considerations

- **Data Caching**: Consider implementing caching for large datasets
- **Lazy Loading**: Implement pagination for very large tables
- **CDN**: Use CDN for static assets in production
- **Database**: For larger datasets, consider moving from CSV to database

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test changes thoroughly

## 🐛 Known Issues

- Data is from 2011 census (consider updating to latest available data)
- Some district names might have spelling variations
- Large state selections may impact performance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Data Source**: Government of India Census 2011
- **Framework**: Plotly Dash community
- **Hosting**: Heroku platform
- **Design Inspiration**: Modern data visualization principles

---

⭐ **Star this repository if you found it helpful!**
