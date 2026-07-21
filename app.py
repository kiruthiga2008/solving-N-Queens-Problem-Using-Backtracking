import streamlit as st

from PROGRAM import solve_n_queens, get_board


st.set_page_config(
    page_title="N-Queens Problem",
    page_icon="♛"
)


st.title("Solving N-Queens Problem using Backtracking")


st.write(
    "Place N queens on an N×N chessboard such that no two queens "
    "share the same row, column, or diagonal."
)


n = st.number_input(
    "Enter the value of N",
    min_value=1,
    max_value=10,
    value=4,
    step=1
)


if st.button("Solve"):

    solutions, backtracks = solve_n_queens(n)

    st.success(
        f"Total Solutions: {len(solutions)}"
    )

    st.info(
        f"Total Backtracks: {backtracks}"
    )


    if len(solutions) == 0:

        st.warning(
            f"No solutions exist for N = {n}"
        )


    else:

        st.subheader(
            f"All Solutions for {n}-Queens"
        )


        for solution_no, solution in enumerate(
            solutions,
            1
        ):

            st.write(
                f"### Solution {solution_no}: {solution}"
            )


            board = get_board(
                solution,
                n
            )


            st.table(board)

            st.divider()
