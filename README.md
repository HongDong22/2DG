기말 프로젝트 준비
======================

# 1. 게임의 소개
## 게임의 제목 - 메이플스토리 (copy)
### 소개
##### 메이플스토리의 점프맵을 모작한 게임으로 캐릭터를 방해물과 패턴을 피하면서 정해진 목적지에 도달하여 보스를 처치한다. 
##### 원게임 스크린 샷 
![표지](https://user-images.githubusercontent.com/56509168/94243092-ea815600-ff51-11ea-9210-fb90bee8b079.PNG)
![321321](https://user-images.githubusercontent.com/56509168/94242726-70e96800-ff51-11ea-9cf7-58d7b5b44859.PNG) 


## 목적
#### 방해와 난관을 뚫어 보스 스테이지로 이동해 보스를 처치한다.

## 방법 
#### A: 왼쪽이동 D:오른쪽 이동 W:포탈 이동  J:점프 K:스킬 L:공격

****
# 2. 각 GameState 별 항목
### GameState (Scene) 의 수 및 각각의 이름
 1.title   
 2.main1   
 3.main2   
 4.boss   
 5.점수판   
 6.옵션   
****
# 3. 각 GameState 별 항목
### 6가지 Scene
* title
   ```
    게임 시작, 게임 이어오기 , 점수판, 종료를 선택할 수 있다.
    ```
 * main1
    ```
    이동키와 점프키만 캐릭터의 상태를 변경. 방해물은 생성되지 않는다
    맵, 캐릭터, 포탈, 시간
    키보드 이벤트 : A,D,W,J 마우스 이벤트:마우스 클릭
    포탈에 W를 눌러 state가 main2로 이동한다.
    설정 아이콘이 클릭 되면 옵션 state로 이동
    ```
    
  * main2
    ```
    main1과 비슷하지만 패턴의 변경과 방해물이 생성된다.
    맵, 캐릭터, 포탈, 방해물, 시간
    키보드 이벤트 : A,D,W,J 마우스 이벤트:마우스 클릭
    포탈에 W를 눌러 state가 boss로 이동한다.
    옵션 아이콘이 클릭 되면 옵션 state로 이동
    ```
    
  * boss
    ```
    공격, 스킬 키가 캐릭터의 상태에 영향을 끼칠 수 있고 보스 몬스터가 생성된다.
    맵, 캐릭터, 보스, 체력, 시간
    키보드 이벤트 : A,D,W,J,K,L 마우스 이벤트:마우스 클릭
    boss 체력이 0이 되면 점수 state로 이동 character 체력 0이 되면 title로 이동
    ```
  * 점수판
    ```
    현재 캐릭터의 체력, 클리어 시간 등을 고려해 점수를 기록하는 곳
    점수, UI
    마우스 클릭을 입력받으면 타이틀 state로 이동
    ```
  * 옵션
    ```
    전 state를 옵션 state의 이벤트에 따라 전 state를 다시 복귀, state 저장, 프로그램 종료, title 이동을 한다.
    설정 UI
    특정 위치 마우스 클릭시 발생하는 이벤트 처리
    ```
    ****
    # 4. 필요한 기술
    ### 다른 과목에서 배운 기술
     ```
     물리학, 프로그래밍, 
     ```
    #### 이 과목에서 배울 것으로 기대되는 기술
     ```
     애니메이션
     입출력 처리
     그래픽 출력
     충돌 검사, 처리
     사운드 처리
     카메라 처리
     게임 저장 기능
     ```
    #### 다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술
     ```
     인공지능 기술
     ```
     
     ****
# 5.개발 계획
   ### 주차별 계획
 1.리소스 수집   
 2.캐릭터 구현  
 3.게임 틀 구현  
 4.방해물, 보스 구현  
 5.캐릭터 추가 구현 및 중간 점검  
 6.방해물 및 보스 추가 구현, 소리 추가 구현  
 7.게임 기능 추가  
 8.마무리  

# 6. 개발 범위
                                          최소 범위                                                                  최대 범위   
![2144444444444444](https://user-images.githubusercontent.com/56509168/95658669-22de8200-0b57-11eb-8ed5-72d7d87c813f.PNG)

    
