py.test ${SRC_DIR}/tests --solver=glpk
py.test ${SRC_DIR}/tests --solver=lpsolve
jupyter nbconvert --to html --execute ${SRC_DIR}/tests/notebook.ipynb
