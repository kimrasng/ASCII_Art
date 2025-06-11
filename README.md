#  ASCII Art

위 프로젝트는 Python으로 만든 터미널 기반 아스키 아트 생성기입니다.
이미지 파일을 불러와 자동으로 크기 조정과 색상 적용을 수행한 후, 터미널에서 색상 아스키 아트로 변환해 출력하고, `.txt` 파일로 저장할 수 있습니다.

## 주요 기능

- 이미지 파일을 컬러 아스키 아트로 변환
- 터미널에 출력 가능
- `.txt` 파일로 추출 가능 (색상은 제거되어 저장됨)
- 사용자 친화적인 CLI 인터페이스 제공
- 경로 입력 시 `~`, `/` 등 사용 가능

## 만들게 된 동기

Python을 이용하여 단순한 이미지들을 텍스트 기반 아트로 표현해보고 싶었습니다. 터미널만으로도 시각적인 창작을 할 수 있다는 점에 매력을 느껴 이 프로젝트를 시작하게 되었습니다.

## 명령어
make, list, print, save, exit
make [name] [image_path] - 새로운 아스키 아트 생성
list - 생성된 아스키 아트 목록 출력
print [name] - 특정 아스키 아트 출력
save [name] - 특정 아스키 아트를 `.txt` 파일로 저장

### example
```bash
make hack-club ./demo/hack-club.png
list
print hack-club
save hack-club
exit
```

## 실행
```bash
python3 ascii_art.py
