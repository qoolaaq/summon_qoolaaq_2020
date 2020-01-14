class Skill:
    """
    各ユニットに持たせるインスタンス
    skill_of_Name で生成する予定
        発動のタイミング
            登場時(CIF: come into field)
            退場時(PIO: placed into outside)
            その他条件(T: trigered)
        ...みたいな感じ
        boolで持たせるべきかも

    """
    def __init__(self):
        self.timing_test = False
        self.test = False
        pass
    def effect(unit):
        """
        unitを引数にする
        実際にはGameControllerで動かすので、
        ゲームロジックで使うインスタンスは引数にしなくてもいいはず
        """
        pass
