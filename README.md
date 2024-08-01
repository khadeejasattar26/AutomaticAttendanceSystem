
**Project Overview**

The Automatic Attendance System utilizes OpenCV for real-time face detection and the Local Binary Patterns Histograms (LBPH) algorithm for accurate face recognition. It aims to revolutionize attendance management in educational institutions and workplaces by providing an efficient and reliable automated solution.

**Features**

1. **Face Detection:** Real-time detection of faces using a webcam or external camera.
2. **Face Recognition:** Identification of individuals through the LBPH algorithm.
3. **Attendance Logging:** Automatic marking and logging of attendance data into a MySQL database.
4. **User Management:** CRUD operations for managing user data, including face capture.
5. **Reporting:** Generation of comprehensive attendance reports based on specified date ranges.

**Modules**

- **Student Details:** Management of user information.
- **Face Detector:** Real-time face detection using OpenCV.
- **Attendance:** Automated attendance marking and logging.
- **Help Desk:** Support module for user assistance.
- **Train Data:** Module for capturing and training face data.
- **Photos:** Storage for face images.
- **Developer Information:** Project contributors and contact details.
- **Exit:** Option to close the application.

**Requirements**

- **Hardware:** Computer with a webcam or external camera.
- **Software:** Python 3.x, OpenCV, NumPy, Pandas, MySQL, Tkinter for GUI, mysql-connector-python.

**Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/khadeejasattar26/AutomaticAttendanceSystem
   cd automatic-attendance-system
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Setup MySQL database:
   - Install MySQL and create a database named `attendance_system`.
   - Run provided SQL script to create necessary tables.
   - Update `config.py` with MySQL database credentials.

**Usage**

1. Run the application:
   ```bash
   python main.py
   ```
2. **Adding Users:**
   - Navigate to user management.
   - Enter details and capture user face.
3. **Marking Attendance:**
   - System automatically detects and logs attendance.
4. **Generating Reports:**
   - Select date range in reports section for attendance reports.

**Project Structure**

- Detailed directory structure and key scripts.
- Configuration files (`config.py`) and setup scripts (`setup_database.py`).

**Contributing**

- Guidelines for contributing to the project.
- Forking, branching, making changes, and creating pull requests.

**License**

- Project licensed under MIT License.
- Reference to `LICENSE` file for details.

**Acknowledgements**

- Acknowledgment of OpenCV and community contributions.

