## 구현할 것

### 1. 로그인 / 비로그인 구분

- articles/create: 
    - 로그인: username 창 생성 되지 않고, request.user의 username 자동 등록
    - 로그아웃: username 창으로 값을 받아서 등록 / 임시 password 창으로 값을 받아서 등록

- articles/detail:
    - 로그인: 비밀번호 창 안 보이게(user의 비밀번호 자동 입력) / 수정﹒삭제 보이게 / 입력한 비밀번호 값 == 해당 글의 비밀번호 값이면, 수정﹒삭제 작동
    - 로그아웃: 비밀번호 창﹒수정﹒삭제 보이게 / 입력한 비밀번호 값 == 해당 글의 비밀번호 값이면, 수정﹒삭제 작동
    - content 최소 높이 설정


### 2. 기능
~~- pagination (10개씩)~~
- search bar (드롭다운: 제목, 내용, 제목+내용)

### 3. 디자인
~~- navbar 로고 옆에 user 이름 띄우기~~