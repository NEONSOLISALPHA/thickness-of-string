from manim import *  # noqa: F403


class Substitute(Scene):
    def construct(self):

        # intro String initialisation
        Intro = Tex(
            '\\emph{Formula for finding thickness of thread: }',
            '\\emph{(Indirectly)}')
        Intro[1]
        In_g = VGroup(Intro[0], Intro[1]).arrange(DOWN, buff=SMALL_BUFF)
        In_g.to_edge(UP)
        In_g.scale(0.9)

        formula = MathTex('\\emph{Thickness}',
                          '\\emph{of}', '\\emph{string}',
                          '=',
                          '{\\emph{length of coil}',
                          '\\over',
                          '\\emph{no. of turns}}')
        formula.scale(1.5)
        formula.shift(RIGHT * 1)

        formula[0].shift(UP * 0.4)
        formula[1].next_to(formula[0], DOWN, buff=SMALL_BUFF)
        formula[2].next_to(formula[1], DOWN, buff=SMALL_BUFF)
        formula[3].next_to(formula[1], RIGHT, buff=1)  # 'of' sign
        formula[5].next_to(formula[3], RIGHT, buff=0.5)
        formula[4].next_to(formula[5], UP, buff=SMALL_BUFF)
        formula[6].next_to(formula[5], DOWN, buff=SMALL_BUFF)

        # for i in [no_of_turns_vg,thickness_vg,length_of_coil_vg,coil_bR,coil_bL,coil_bD,coil]: # noqa: E501
        #     i.shift(RIGHT*5)
        #     i.generate_target()
        #     i.target.shift(LEFT*5)

        for i in formula[:4]:
            i.shift(LEFT * 8)
            i.generate_target()
            i.target.shift(RIGHT * 8)

        for i in formula[4:]:
            i.shift(RIGHT * 8)
            i.generate_target()
            i.target.shift(LEFT * 8)

        # formula.shift(RIGHT*11)
        # formula.generate_target()
        # formula.target.shift(LEFT*11)

        self.play(*[MoveToTarget(i) for i in formula[:4]],
                  *[MoveToTarget(i) for i in formula[4:]])
        self.wait(2)
        val_coil_length = 40
        val_no_of_turns = 50
        val_answer = round(val_coil_length / val_no_of_turns, 3)

        ans_formula = MathTex('\\emph{Thickness}',
                              '\\emph{of}',
                              '\\emph{string}',
                              '=', '{' + str(val_coil_length),
                              '\\over', str(val_no_of_turns) + '}',
                              f'{val_answer} mm')
        ans_formula.scale(1.5)
        ans_formula.shift(RIGHT * 1)

        ans_formula[0].shift(UP * 0.4)
        ans_formula[1].next_to(ans_formula[0], DOWN, buff=SMALL_BUFF)
        ans_formula[2].next_to(ans_formula[1], DOWN, buff=SMALL_BUFF)
        ans_formula[3].next_to(ans_formula[1], RIGHT, buff=1)  # 'of' sign
        ans_formula[5].next_to(ans_formula[3], RIGHT, buff=0.5)
        ans_formula[4].next_to(ans_formula[5], UP, buff=SMALL_BUFF)
        ans_formula[6].next_to(ans_formula[5], DOWN, buff=SMALL_BUFF)
        ans_formula[7].next_to(ans_formula[3], RIGHT, buff=0.7)
        ans_formula[7].next_to(ans_formula[3], RIGHT, buff=0.7)
        ans_formula[7].set_color(GREEN)  # type: ignore # noqa: E501
        # ans_formula[8].next_to(ans_formula[7],RIGHT,buff=1).scale(1.2)

        changes = [(0, 1, 2, 3, 4, 5, 6),
                   (0, 1, 2, 3, 4, 5, 6)]
        self.play(
            *[ReplacementTransform(formula[i], ans_formula[j]) for i, j in zip(changes[0], changes[1])]  # noqa: E501
        )

        self.wait()

        self.play(FadeOutAndShift(ans_formula[4:7], UP), FadeInFrom(
            ans_formula[7], RIGHT))
        self.wait()

        self.play(*[Uncreate(i) for i in [ans_formula[0], ans_formula[1],
                                          ans_formula[2], ans_formula[3],
                                          ans_formula[7]]])
        self.wait()

        bye = Tex('Thanks for Watching!').scale(2.5)

        self.play(Write(bye))
        self.wait()

        self.play(Uncreate(bye))

        name = Tex('Adithyadev R')
        Class = Tex('Class \\rm X\\rm I \\rm A')
        name_class = VGroup(name, Class).arrange(DOWN).scale(2)

        self.play(Write(name_class))
        self.wait()

        self.play(Uncreate(name_class))
        self.wait()
