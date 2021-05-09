def 黙示録(word):
    wrong=0
    stages=["",
            "私の耳に雷鳴が響き、",
            "第四の生き物が「来たれ」といった。",
            "すると、",
            "見よ、",
            "青白い馬だ。",
            "それに乗る者の名は『死』、",
            "付添うは『黄泉』。"
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("黙示録へようこそ！")

    while wrong<len(stages)-1:
        #lenは、リストの要素を数えてくれる関数。
        print("\n")
        character=input("１文字を予想して入力してね：")
        #テキストではboardの［］の中身に、別で用意したものを代入していた。
        #わかりにくいため直接入れてみたが、それでもきちんと機能した。
        if character in rletters:
            board[rletters.index(character)]=character
            #indexメソッドはリストの最初から当てはめていくため、以上のままだと、同じ文字が複数ある場合は後の文字までたどり着かない。
            #それを改善するには最初の文字が正解した後で、最初の文字を"別の文字(テキストでは$)"に変更しておく。そうするとindexはそれを飛ばして次の空欄を検索してくれる。
            rletters[rletters.index(character)]='＠'

        else:
            wrong +=1
        print(" ".join(board))

        e=wrong+1
        print("\n".join(stages[0:e]))

        if "_"not in board:
            print("あなたの勝ち！正解は、")
            print(" ".join(board))

            win=True

            break
    if not win:
        print("あなたの負け！正解は{}。".format(word))
        #テキストでは負けの際の全文表示が[0:wrong+1]となっていたが、下でOK。
        print("\n".join(stages))

黙示録("terminater")
