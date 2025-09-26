// 인증 관련 JavaScript

class AuthManager {
    constructor() {
        this.currentUser = null;
        this.init();
    }

    async init() {
        await this.checkAuthStatus();
    }

    async checkAuthStatus() {
        try {
            const response = await fetch('/auth/check_auth');
            const data = await response.json();
            
            if (data.authenticated) {
                this.currentUser = data.user;
                this.updateUIForLoggedInUser();
            } else {
                this.updateUIForLoggedOutUser();
            }
        } catch (error) {
            console.error('인증 상태 확인 실패:', error);
        }
    }

    async login(username, password) {
        try {
            const response = await fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();
            
            if (response.ok) {
                this.currentUser = data.user;
                this.updateUIForLoggedInUser();
                this.showMessage('로그인 성공!', 'success');
                return true;
            } else {
                this.showMessage(data.error, 'error');
                return false;
            }
        } catch (error) {
            console.error('로그인 실패:', error);
            this.showMessage('로그인 중 오류가 발생했습니다.', 'error');
            return false;
        }
    }

    async register(username, email, password, role = 'user') {
        try {
            const response = await fetch('/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, password, role })
            });

            const data = await response.json();
            
            if (response.ok) {
                this.showMessage('회원가입 성공! 로그인해주세요.', 'success');
                return true;
            } else {
                this.showMessage(data.error, 'error');
                return false;
            }
        } catch (error) {
            console.error('회원가입 실패:', error);
            this.showMessage('회원가입 중 오류가 발생했습니다.', 'error');
            return false;
        }
    }

    async logout() {
        try {
            const response = await fetch('/auth/logout', {
                method: 'POST'
            });

            if (response.ok) {
                this.currentUser = null;
                this.updateUIForLoggedOutUser();
                this.showMessage('로그아웃되었습니다.', 'success');
            }
        } catch (error) {
            console.error('로그아웃 실패:', error);
        }
    }

    updateUIForLoggedInUser() {
        // 로그인 버튼을 사용자 정보로 변경
        const loginButton = document.getElementById('login-btn');
        if (loginButton) {
            loginButton.innerHTML = `
                <span>${this.currentUser.username}</span>
                <button onclick="authManager.logout()" class="logout-btn">로그아웃</button>
            `;
        }

        // 관리자 메뉴 표시
        if (this.currentUser.role === 'admin') {
            const adminMenu = document.getElementById('admin-menu');
            if (adminMenu) {
                adminMenu.style.display = 'block';
            }
        }
    }

    updateUIForLoggedOutUser() {
        // 로그인 버튼 표시
        const loginButton = document.getElementById('login-btn');
        if (loginButton) {
            loginButton.innerHTML = '<button onclick="showLoginModal()">로그인</button>';
        }

        // 관리자 메뉴 숨기기
        const adminMenu = document.getElementById('admin-menu');
        if (adminMenu) {
            adminMenu.style.display = 'none';
        }
    }

    showMessage(message, type) {
        // 메시지 표시 (기존 메시지 시스템 사용)
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.textContent = message;
        
        document.body.appendChild(messageDiv);
        
        setTimeout(() => {
            messageDiv.remove();
        }, 3000);
    }

    isLoggedIn() {
        return this.currentUser !== null;
    }

    isAdmin() {
        return this.currentUser && this.currentUser.role === 'admin';
    }
}

// 전역 인스턴스 생성
const authManager = new AuthManager();

// 로그인 모달 표시
function showLoginModal() {
    const modal = document.getElementById('login-modal');
    if (modal) {
        modal.style.display = 'block';
    }
}

// 회원가입 모달 표시
function showRegisterModal() {
    const modal = document.getElementById('register-modal');
    if (modal) {
        modal.style.display = 'block';
    }
}

// 모달 닫기
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

// 로그인 폼 제출
async function handleLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get('username');
    const password = formData.get('password');
    
    const success = await authManager.login(username, password);
    if (success) {
        closeModal('login-modal');
    }
}

// 회원가입 폼 제출
async function handleRegister(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get('username');
    const email = formData.get('email');
    const password = formData.get('password');
    const role = formData.get('role') || 'user';
    
    const success = await authManager.register(username, email, password, role);
    if (success) {
        closeModal('register-modal');
    }
}


