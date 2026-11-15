"""Pruebas con datos artificiales mínimos; no representan resultados del caso."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import pandas as pd
import numpy as np

NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks/connectatel_analysis.ipynb"
CELLS = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]

def run_cell(index, env):
    exec("".join(CELLS[index]["source"]), env)

class AnalysisTests(unittest.TestCase):
    def test_code_compiles(self):
        for i, cell in enumerate(CELLS):
            if cell["cell_type"] == "code":
                compile("".join(cell["source"]), f"cell_{i}", "exec")

    def test_missing_files_actionable(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict("os.environ", {"CONNECTATEL_DATA_DIR": folder}):
                with self.assertRaisesRegex(FileNotFoundError, "Faltan"):
                    run_cell(4, {"pd": pd})

    def test_aggregation_and_segments(self):
        users = pd.DataFrame({"user_id": [1, 2, 3], "age": [29, 60, np.nan]})
        usage = pd.DataFrame({
            "user_id": [1, 1, 1, 1],
            "type": ["call", "text", "call", "call"],
            "date": pd.to_datetime(["2024-01-01", "2024-01-02", "2025-01-01", None]),
            "duration": [10, 999, 100, 100]})
        env = {"pd": pd, "np": np, "users": users, "usage": usage}
        for index in [45, 46, 47, 67, 70]:
            run_cell(index, env)
        result = env["user_profile"].set_index("user_id")
        self.assertEqual(result.loc[1, "cant_minutos_llamada"], 10)
        self.assertEqual(result.loc[1, "cant_llamadas"], 1)
        self.assertEqual(result.loc[1, "cant_mensajes"], 1)
        self.assertEqual(result.loc[2, "cant_llamadas"], 0)
        self.assertEqual(result.loc[2, "grupo_uso"], "Bajo uso")
        self.assertEqual(result.loc[3, "grupo_edad"], "Sin dato")

    def test_missing_call_duration_rejected(self):
        env = {"pd": pd, "usage": pd.DataFrame({
            "user_id": [1], "type": ["call"],
            "date": pd.to_datetime(["2024-01-01"]), "duration": [None]})}
        with self.assertRaisesRegex(ValueError, "duración"):
            run_cell(45, env)

if __name__ == "__main__":
    unittest.main()
