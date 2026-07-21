import streamlit as st
from program import solve_n_queens, get_board


# Page Configuration
st.set_page_config(
    page_title="N-Queens Backtracking",
    page_icon="♛",
    layout="wide"
)


# Title
st.title("♛ Solving N-Queens Problem Using Backtracking")

st.markdown(
    """
    The **N-Queens Problem** places N queens on an N × N chessboard
    such that no two queens attack each other.

    A queen must not share the same:

    - Row
    - Column
    - Diagonal

    This application solves the problem using the **Backtracking technique**.
    """
)


# Sidebar
st.sidebar.header("N-Queens Configuration")

n = st.sidebar.slider(
    "Select Board Size (N)",
    min_value=1,
    max_value=10,
    value=4
)


solve_button = st.sidebar.button("Solve N-Queens")


# Solve the problem
if solve_button:

    with st.spinner("Finding all possible solutions..."):

        solutions, backtracks = solve_n_queens(n)

    st.success("Solution search completed successfully!")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Board Size",
            value=f"{n} × {n}"
        )

    with col2:
        st.metric(
            label="Total Solutions",
            value=len(solutions)
        )

    with col3:
        st.metric(
            label="Backtracks",
            value=backtracks
        )


    st.divider()


    # No solution case
    if len(solutions) == 0:

        st.warning(
            f"No valid solutions exist for {n}-Queens."
        )


    else:

        st.subheader(
            f"All Solutions for {n}-Queens"
        )


        # Solution selector
        solution_number = st.number_input(
            "Select Solution Number",
            min_value=1,
            max_value=len(solutions),
            value=1,
            step=1
        )


        selected_solution = solutions[solution_number - 1]


        st.write(
            f"### Solution {solution_number}"
        )


        st.write(
            f"Position Representation: `{selected_solution}`"
        )


        # Display board
        board = get_board(
            selected_solution,
            n
        )


        # Create visual chessboard using columns
        for row in range(n):

            cols = st.columns(n)

            for col in range(n):

                with cols[col]:

                    if board[row][col] == "Q":

                        st.markdown(
                            """
                            <div style="
                                background-color:#ff4b4b;
                                height:60px;
                                display:flex;
                                align-items:center;
                                justify-content:center;
                                font-size:35px;
                                border:1px solid black;
                            ">
                            ♛
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            """
                            <div style="
                                background-color:#f0f0f0;
                                height:60px;
                                display:flex;
                                align-items:center;
                                justify-content:center;
                                font-size:35px;
                                border:1px solid black;
                            ">
                            ·
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


        st.divider()


        # Show all solutions for small boards
        if n <= 6:

            st.subheader("Solution Summary")

            for i, solution in enumerate(solutions, 1):

                st.write(
                    f"Solution {i}: `{solution}`"
                )


# Default information
else:

    st.info(
        "Select the board size from the sidebar and click "
        "'Solve N-Queens' to find all valid solutions."
    )


# Algorithm Explanation
st.divider()

st.subheader("How Backtracking Works")

st.markdown(
    """
    1. Start from the first row.
    2. Try placing a queen in every column.
    3. Check whether the position is safe.
    4. If safe, move to the next row.
    5. If no valid position is possible, undo the previous placement.
    6. Continue until all queens are placed.
    """
)


st.subheader("Complexity Analysis")

st.markdown(
    """
    - **Worst-case Time Complexity:** O(N!)
    - **Space Complexity:** O(N)
    - **Technique Used:** Backtracking
    - **Constraint Checking:** Column and diagonal checking
    """
)
