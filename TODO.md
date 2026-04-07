# MongoDB Configuration TODO

**Approved Plan Steps:**

## 1. Setup Virtual Environment & Install Dependencies ✅ Completed

## 2. Update settings.py ✅ Completed

## 3. Test Migration
- `python notice_board/manage.py makemigrations notices`
- `python notice_board/manage.py migrate`

## 4. Run & Test
- `python notice_board/manage.py runserver`
- Verify MongoDB connection (admin, create notice).

## 5. Cleanup (optional)
- Delete db.sqlite3
