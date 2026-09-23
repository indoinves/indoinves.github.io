# ==============================================================================
# Makefile untuk Proyek IndoInves
# ==============================================================================

.PHONY: help run-python run-go run-node clean status

# Menampilkan bantuan perintah yang tersedia
help:
	@echo "=================================================="
	@echo "Daftar Perintah Makefile IndoInves:"
	@echo "=================================================="
	@echo "  make run-python  - Menjalankan server Flask (Python)"
	@echo "  make run-go      - Menjalankan server Go"
	@echo "  make run-node    - Menjalankan server Node.js (Express)"
	@echo "  make clean       - Membersihkan file sampah/cache proyek"
	@echo "  make status      - Mengecek status file git"
	@echo "=================================================="

# Menjalankan versi Python (Flask)
run-python:
	@echo "Menjalankan server Python..."
	python3 app.py

# Menjalankan versi Golang
run-go:
	@echo "Menjalankan server Go..."
	go run main.go

# Menjalankan versi Node.js
run-node:
	@echo "Menjalankan server Node.js..."
	node server.js

# Membersihkan file cache atau sisa build
clean:
	@echo "Membersihkan file cache..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Pembersihan selesai!"

# Mengecek status repositori Git
status:
	git status
