import math

class Skill:
    """
    各ユニットに持たせるインスタンス
    SkillOfName クラスで継承して、
    skill_of_Name インスタンスを生成する。
        発動のタイミング
            登場時(CIF: come into field)
            退場時(PIO: placed into outside)
            その他条件(T: trigered)
        ...みたいな感じ
        boolで持たせるべきかも
    """
    def __init__(self):
        self.timing_CIF = False
        self.timing_PIO = False
        self.unit = None
    def is_activated(self, timing_type):
        """
        timing_type: str を引っ張ってきて
        自身のtiming_typeを返す
        """
        if timing_type == "CIF":
            return self.timing_CIF
        elif timing_type == "PIO":
            return self.timing_PIO
        # この下を拡張していく予定(2020/01/19)
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        """
        実際にはGameControllerで動かすので、
        ゲームロジックで使うインスタンスは引数にしなくてもいいはず
            そんなことはなかった(2020/01/19)
        """
        pass
    def get_unit(self, unit):
        """
        skillのプロパティとしてunitを持たせる
        """
        self.unit = unit

