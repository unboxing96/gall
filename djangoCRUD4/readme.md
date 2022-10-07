# 멀캠 갤러리 설계

## nav
- 전체글
- 개념글 
- 공지

## index

- table
    - 글 번호
    - 제목
    - 글쓴이
    - 작성일 (당일은 시간, 이전은 날짜)
    - 조회수
    - 추천수

- footer
    - foot nav
        - 전체글 (L)
        - 개념글 (L)
        - 글쓰기 (R)
    
    - paginataion
        - 1~15까지 표시
        - 15번 오른쪽에 [다음 페이지], [마지막 페이지]
    
    - search bar
        - 제목/내용/글쓴이 dropdown
        - 검색창

## detail

- nav
    - 로고 이미지 (index.html)

- main
    - title
    - user_id | created_at
    - view_cnt | thumb_up_cnt | comment_cnt
    __________
    - content 
    - thumb_up / thumb_down
    __________
    - comment
    - comment_form
    __________

- foot nav
    - 전체글 (L)
    - 개념글 (L)
    - 수정 (R)
    - 삭제 (R)
    - 글쓰기 (R)

## create

- nav
    - 로고 이미지 (index.html)

- user form
    - user_id
    - user_pw
    - title

- content form
    - file: image

- foot nav
    - 취소 (R)
    - 등록 (R)


