- [keymouse](#keymouse)
  - [TODO](#todo)
  - [빌드](#빌드)
  - [윈도우 시작프로그램에 추가](#윈도우-시작프로그램에-추가)
  - [기능](#기능)

# keymouse

keyboard를 mouse로 이용하자

## TODO

- noti기능
  - logfile 외에 toast나 alert해주기(toggle_mode에만 넣으면 될듯?)

## 빌드

pyinstaller main.spec

## 윈도우 시작프로그램에 추가

- keymouse.bat 바로가기 만들기
- win+r 에서 shell:startup의 경로에 바로가기 잘라내기

## 기능

1. toggle_mode('keyboard', 'mouse')
   1. keyboard 모드는 키보드와 동일
   2. mouse 모드 진입시 키보드를 마우스처럼 쓸 수 있다
2. move_mouse
   1. vim처럼 h,j,k,l로 움직인다
   2. 세밀하게 움직이려면 ctrl키를 누른채로
3. scroll_mouse
   1. u,i로 스크롤한다
   2. 세밀하게 움직이려면 ctrl키를 누른채로
4. click mouse
   1. c를 누르면 클릭한다
