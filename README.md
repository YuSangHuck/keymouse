- [requirement](#requirement)
- [keymouse](#keymouse)
  - [TODO](#todo)
  - [빌드](#빌드)
  - [사용법](#사용법)
  - [기능](#기능)

# requirement

- Python 3.11.9

# keymouse

- 침대에서 컴퓨터가 하고싶다..
- keyboard를 mouse로 이용하자...!

## TODO

- kill signal handler?
  - log 및 noti?

## 빌드

pyinstaller main.spec

## 사용법

- keymouse.bat 파일을 통해 keymouse 프로세스를 on/off한다

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
