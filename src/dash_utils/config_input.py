import pandas as pd


class MLXL_Config:

    def __init__(self):
        self._status = pd.DataFrame(columns=[
            'process_run_id', 'process_datetime', 'process_version', 'process_type', 'process_config_json', 'process_status'])

        self._dt_current_version = 0.0
        self._dt_serial_number = 1
        self._dt_initial_status = 'Initialization'

        self._fs_current_version = 0.0
        self._fs_serial_number = 1
        self._fs_initial_status = 'Initialization'

        self._bm_current_version = 0.0
        self._bm_serial_number = 1
        self._bm_initial_status = 'Initialization'

    @property
    def status(self) -> pd.DataFrame:
        return self._status

    @status.setter
    def status(self, dataframe: pd.DataFrame) -> None:
        self._status = dataframe

    @property
    def dt_current_version(self) -> float:
        return self._dt_current_version

    @dt_current_version.setter
    def dt_current_version(self, version: float) -> None:
        self._dt_current_version = version

    @property
    def dt_serial_number(self) -> int:
        return self._dt_serial_number

    @dt_serial_number.setter
    def dt_serial_number(self, serial_number: int) -> None:
        self._dt_serial_number = serial_number

    @property
    def dt_initial_status(self) -> str:
        return self._dt_initial_status

    @dt_initial_status.setter
    def dt_initial_status(self, status: str) -> None:
        self._dt_initial_status = status

    # ------------------------- FEATURE SELECTION -------------------------

    @property
    def fs_current_version(self) -> float:
        return self._fs_current_version

    @fs_current_version.setter
    def fs_current_version(self, version: float) -> None:
        self._fs_current_version = version

    @property
    def fs_serial_number(self) -> int:
        return self._fs_serial_number

    @fs_serial_number.setter
    def fs_serial_number(self, serial_number: int) -> None:
        self._fs_serial_number = serial_number

    @property
    def fs_initial_status(self) -> str:
        return self._fs_initial_status

    @fs_initial_status.setter
    def fs_initial_status(self, status: str) -> None:
        self._fs_initial_status = status

    # ------------------------- FEATURE SELECTION -------------------------

    @property
    def bm_current_version(self) -> float:
        return self._bm_current_version

    @bm_current_version.setter
    def bm_current_version(self, version: float) -> None:
        self._bm_current_version = version

    @property
    def bm_serial_number(self) -> int:
        return self._bm_serial_number

    @bm_serial_number.setter
    def bm_serial_number(self, serial_number: int) -> None:
        self._bm_serial_number = serial_number

    @property
    def bm_initial_status(self) -> str:
        return self._bm_initial_status

    @bm_initial_status.setter
    def bm_initial_status(self, status: str) -> None:
        self._bm_initial_status = status


class EDAToolConfig:

    def __init__(self):
        self._raw_data = pd.DataFrame()

    @property
    def raw_data(self) -> pd.DataFrame:
        return self._raw_data

    @raw_data.setter
    def raw_data(self, dataframe: pd.DataFrame) -> None:
        self._raw_data = dataframe


class DataTransformConfig:

    def __init__(self):

        self._transform_method: list = [
            'drop_redundent_columns',
            'drop_null_columns',
            'drop_unique_value_columns',
            'data_imputation',
            'feature_scaling',
            'feature_transformer'
        ]

        self._imputation_methods: list = [
            'iterative', 'knn', 'simple'
        ]

        self._feature_scaling_methods: list = [
            'standard', 'robust', 'minmax', 'maxabs'
        ]

        self._feature_transform_methods: list = [
            'power', 'quantile'
        ]

        self.dt_conf_input: dict = {
            'file_path': '',
            'file_type': '',
            'target_feature': '',
            'feature_list': [],
            'transform_conf': [],
            'remove_outlier': False,
            'contamination_factor': 0,
            'save_path': './data/downloadables/data_transform_files/transform_pipeline.joblib'
        }

        self._raw_data = pd.DataFrame()

    @property
    def transform_method(self) -> list:
        return self._transform_method

    @property
    def imputation_methods(self) -> list:
        return self._imputation_methods

    @property
    def feature_scaling_methods(self) -> list:
        return self._feature_scaling_methods

    @property
    def feature_transform_methods(self) -> list:
        return self._feature_transform_methods

    @property
    def raw_data(self) -> pd.DataFrame:
        return self._raw_data

    @raw_data.setter
    def raw_data(self, dataframe: pd.DataFrame) -> None:
        self._raw_data = dataframe

    def refresh_config(self):
        self.dt_conf_input = {
            'file_path': '',
            'file_type': '',
            'target_feature': '',
            'feature_list': [],
            'transform_conf': [],
            'remove_outlier': False,
            'contamination_factor': 0,
            'save_path': './data/downloadables/data_transform_files/transform_pipeline.joblib'
        }


class FeatureSelectionConfig:

    def __init__(self):

        self._selection_methods = [
            'anova_f_value_selection',
            'mutual_info_classif_selection',
            'logit_selection',
            'permutation_impt_selection',
            'recursive_feature_elimination',
            'model_based_importance',
            'regularization_selection',
            'boruta_selection',
            'sequencial_forward_selection'
        ]

        self._correlation_methods = [
            'pearson', 'kendall', 'spearman'
        ]

        self._logit_fit_methods = [
            'default', 'newton', 'bfgs', 'lbfgs', 'powell', 'cg', 'ncg', 'basinhopping'
        ]

        self._perm_impt_model_list = [
            'random_forest', 'catboost', 'xgboost', 'lightgbm', 'gradient_boosting', 'logistic_regression', 'all'
        ]

        self._rfe_model_list = [
            'random_forest', 'catboost', 'xgboost', 'lightgbm', 'gradient_boosting', 'logistic_regression', 'all'
        ]

        self._model_based_impt_model_list = [
            'random_forest', 'catboost', 'xgboost', 'lightgbm', 'all'
        ]

        self._reg_based_model_list = [
            'lasso', 'ridge', 'elasticnet', 'all'
        ]

        self._boruta_model_list = [
            'random_forest', 'xgboost', 'lightgbm', 'gradient_boosting', 'all'
        ]

        self._sfs_model_list = [
            'random_forest', 'xgboost', 'lightgbm', 'gradient_boosting', 'all'
        ]

        self._sfs_scoring_metrics = [
            'accuracy', 'roc_auc', 'precision', 'recall', 'f1'
        ]

        self.fs_conf_input: dict = {
            'file_path': '',
            'file_type': '',
            'target_feature': '',
            'run_parallel': True,

            'drop_low_variance_features': False,
            'variance_thresh': 0.0,

            'drop_high_corr_features': False,
            'corr_threshold': 0.0,
            'corr_method': '',

            'drop_multicolliner_features': False,

            'feature_select_conf': [],
            'test_size': 0.0,
            'save_path': './data/downloadables/feature_selection_files/feature_selected_meta.joblib'
        }

        self._transformed_data = pd.DataFrame()

    @property
    def transformed_data(self) -> pd.DataFrame:
        return self._transformed_data

    @transformed_data.setter
    def transformed_data(self, dataframe: pd.DataFrame) -> None:
        self._transformed_data = dataframe

    @property
    def selection_methods(self) -> list:
        return self._selection_methods

    @property
    def correlation_methods(self) -> list:
        return self._correlation_methods

    @property
    def logit_fit_methods(self) -> list:
        return self._logit_fit_methods

    @property
    def perm_impt_model_list(self) -> list:
        return self._perm_impt_model_list

    @property
    def rfe_model_list(self) -> list:
        return self._rfe_model_list

    @property
    def model_based_impt_model_list(self) -> list:
        return self._model_based_impt_model_list

    @property
    def reg_based_model_list(self) -> list:
        return self._reg_based_model_list

    @property
    def boruta_model_list(self) -> list:
        return self._boruta_model_list

    @property
    def sfs_model_list(self) -> list:
        return self._sfs_model_list

    @property
    def sfs_scoring_metrics(self) -> list:
        return self._sfs_scoring_metrics

    def refresh_config(self):
        self.fs_conf_input = {
            'file_path': '',
            'file_type': '',
            'target_feature': '',
            'run_parallel': True,

            'drop_low_variance_features': False,
            'variance_thresh': 0.0,

            'drop_high_corr_features': False,
            'corr_threshold': 0.0,
            'corr_method': '',

            'drop_multicolliner_features': False,

            'feature_select_conf': [],
            'test_size': 0.0,
            'save_path': './data/downloadables/feature_selection_files/feature_selected_meta.joblib'
        }


class BaselineModelingConfig:

    def __init__(self):
        self.bm_conf_input = {
            'file_path': {
                'X_train': '',
                'y_train': '',
                'selected_feature': ''
            },

            'balanced_data': False,
            'check_imbalance': False,
            'imbalance_class': 1,
            'imbalance_threshold': 0.0,

            'feature_set_list': [],
            'model_list': [],
            'sample_list': [],

            'enable_voting': False,
            'voting_model_list': [],
            'voting_sample_list': [],

            'kpi_sorting': [],
            'save_path': {
                'report': './data/downloadables/baseline_modeling_files/baseline_results.xlsx',
                'best_results': './data/downloadables/baseline_modeling_files/baseline_best_results.joblib'
            }
        }

        self._model_list = [
            'random_forest', 'gradient_boosting', 'xgboost', 'lightgbm', 'logistic_regression', 'svm_rbf', 'mlp_classifier', 'all'
        ]

        self._sample_list = [
            'smote (up)', 'adasyn (up)', 'svm_smote (up)', 'boderline_smote (up)', 'k_means_smote (up)', 'near_miss (down)',
            'renn (down)', 'tomek_links (down)', 'smote_tomek (combine)', 'smote_enn (combine)', 'all'
        ]

        self._kpi_list = [
            'accuracy', 'precision', 'recall', 'f1', 'f2', 'f0.5', 'roc_auc',
        ]

        self._selected_features = pd.DataFrame()
        self._x_train = pd.DataFrame()
        self._y_train = pd.DataFrame()

    @property
    def model_list(self) -> list:
        return self._model_list

    @property
    def sample_list(self) -> list:
        return self._sample_list

    @property
    def kpi_list(self) -> list:
        return self._kpi_list

    @property
    def selected_features(self) -> pd.DataFrame:
        return self._selected_features

    @selected_features.setter
    def selected_features(self, dataframe: pd.DataFrame) -> None:
        self._selected_features = dataframe

    @property
    def x_train(self) -> pd.DataFrame:
        return self._x_train

    @x_train.setter
    def x_train(self, dataframe: pd.DataFrame) -> None:
        self._x_train = dataframe

    @property
    def y_train(self) -> pd.DataFrame:
        return self._y_train

    @y_train.setter
    def y_train(self, dataframe: pd.DataFrame) -> None:
        self._y_train = dataframe

    def refresh_config(self):
        self.bm_conf_input = {
            'file_path': {
                'X_train': '',
                'y_train': '',
                'selected_feature': ''
            },

            'balanced_data': False,
            'check_imbalance': False,
            'imbalance_class': 1,
            'imbalance_threshold': 0.0,

            'feature_set_list': [],
            'model_list': [],
            'sample_list': [],

            'enable_voting': False,
            'voting_model_list': [],
            'voting_sample_list': [],

            'kpi_sorting': [],
            'save_path': {
                'report': './data/baseline_results_v1.xlsx',
                'best_results': './data/baseline_best_results_v1.joblib'
            }
        }


eda_conf = EDAToolConfig()
dt_conf = DataTransformConfig()
fs_conf = FeatureSelectionConfig()
bm_conf = BaselineModelingConfig()
ml_config = MLXL_Config()
