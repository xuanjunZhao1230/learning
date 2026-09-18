"""
代码题：班级成绩分析器（难度：适中）

题目背景
--------
学校需要一个简单的班级成绩分析程序。请使用面向对象编程完成学生成绩的
录入、排名和统计。

任务要求
--------
1. 定义 Student（学生）类：
   - 保存学生姓名和各科成绩，成绩使用字典存储。
   - 提供录入成绩的方法；科目必须属于班级规定的科目，成绩必须在 0~100 之间。
   - 使用 @property 定义 average 属性，返回该学生已录入科目的平均分。
   - 提供判断是否已录完全部科目的方法。

2. 定义 GradeBook（成绩册）类：
   - 使用字典保存所有学生，使用集合保存班级规定的科目。
   - 可以添加学生，但不允许出现重名学生。
   - 可以根据“姓名、科目、分数”录入成绩。
   - 生成完整成绩排名：只统计已录完全部科目的学生，按平均分从高到低排序；
     平均分相同时按姓名升序排列。
   - 统计指定科目的平均分、最高分和最低分。
   - 找出优秀学生：全部科目已录入、平均分不低于 85 分，且每科不低于 80 分。
   - 输出完整的班级成绩报告，并指出成绩尚未录完的学生。

3. 使用题目给出的测试数据运行程序。

主要考查知识点
--------------
类和对象、封装、@property、列表、字典、集合、函数、分支与循环、
列表生成式、lambda 排序、字符串格式化。

建议：先根据上面的要求独立完成，再阅读下方参考答案。
"""


class Student:
    """学生类：保存一名学生的姓名和成绩。"""

    def __init__(self, name):
        self.name = name
        self.scores = {}

    def record_score(self, subject, score, allowed_subjects):
        """录入一科成绩；成功返回 True，数据不合法返回 False。"""
        if subject not in allowed_subjects:
            return False
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            return False
        if score < 0 or score > 100:
            return False
        self.scores[subject] = score
        return True

    @property
    def average(self):
        """返回已录入科目的平均分；没有成绩时返回 0。"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def is_complete(self, required_subjects):
        """判断规定科目的成绩是否已经全部录入。"""
        return required_subjects <= set(self.scores)

    def missing_subjects(self, required_subjects):
        """返回还未录入成绩的科目集合。"""
        return required_subjects - set(self.scores)


class GradeBook:
    """班级成绩册。"""

    def __init__(self, class_name, subjects):
        self.class_name = class_name
        self.subjects = set(subjects)
        self.students = {}

    def add_student(self, name):
        """添加学生；姓名为空或重名时返回 False。"""
        name = name.strip()
        if not name or name in self.students:
            return False
        self.students[name] = Student(name)
        return True

    def record_score(self, name, subject, score):
        """为指定学生录入成绩。"""
        student = self.students.get(name)
        if student is None:
            return False
        return student.record_score(subject, score, self.subjects)

    def get_rankings(self):
        """返回已录完全部科目的学生排名。"""
        complete_students = [
            student
            for student in self.students.values()
            if student.is_complete(self.subjects)
        ]
        return sorted(
            complete_students,
            key=lambda student: (-student.average, student.name)
        )

    def subject_statistics(self, subject):
        """返回指定科目的平均分、最高分和最低分。"""
        if subject not in self.subjects:
            return None

        scores = [
            student.scores[subject]
            for student in self.students.values()
            if subject in student.scores
        ]
        if not scores:
            return None

        return {
            'average': sum(scores) / len(scores),
            'highest': max(scores),
            'lowest': min(scores)
        }

    def get_excellent_students(self):
        """返回平均分不低于 85 且每科不低于 80 的完整成绩学生。"""
        excellent_students = []
        for student in self.students.values():
            if not student.is_complete(self.subjects):
                continue
            if student.average >= 85 and min(student.scores.values()) >= 80:
                excellent_students.append(student)
        return sorted(excellent_students, key=lambda student: student.name)

    def print_report(self):
        """输出排名、单科统计、优秀学生和未完成录入名单。"""
        print(f'===== {self.class_name}成绩报告 =====')

        print('\n【总分排名】')
        rankings = self.get_rankings()
        if not rankings:
            print('暂无完整成绩')
        else:
            for rank, student in enumerate(rankings, start=1):
                score_text = '，'.join(
                    f'{subject}：{student.scores[subject]}'
                    for subject in sorted(self.subjects)
                )
                print(
                    f'{rank}. {student.name} | {score_text} | '
                    f'平均分：{student.average:.2f}'
                )

        print('\n【单科统计】')
        for subject in sorted(self.subjects):
            statistics = self.subject_statistics(subject)
            if statistics is None:
                print(f'{subject}：暂无成绩')
            else:
                print(
                    f"{subject}：平均分 {statistics['average']:.2f}，"
                    f"最高分 {statistics['highest']}，"
                    f"最低分 {statistics['lowest']}"
                )

        print('\n【优秀学生】')
        excellent_students = self.get_excellent_students()
        if excellent_students:
            print('、'.join(student.name for student in excellent_students))
        else:
            print('暂无')

        print('\n【成绩未录完】')
        incomplete_students = [
            student
            for student in self.students.values()
            if not student.is_complete(self.subjects)
        ]
        if not incomplete_students:
            print('无')
        else:
            for student in sorted(incomplete_students, key=lambda item: item.name):
                missing = '、'.join(sorted(student.missing_subjects(self.subjects)))
                print(f'{student.name}：缺少 {missing}')


def main():
    """使用给定数据演示成绩分析器。"""
    grade_book = GradeBook('Python 初级班', {'语文', '数学', '英语'})

    score_data = {
        '张三': {'语文': 88, '数学': 92, '英语': 84},
        '李四': {'语文': 95, '数学': 80, '英语': 89},
        '王五': {'语文': 76, '数学': 90, '英语': 81},
        '赵六': {'语文': 91, '数学': 87, '英语': 96},
        '钱七': {'语文': 100, '数学': 60}
    }

    for name, scores in score_data.items():
        grade_book.add_student(name)
        for subject, score in scores.items():
            grade_book.record_score(name, subject, score)

    grade_book.print_report()


if __name__ == '__main__':
    main()
