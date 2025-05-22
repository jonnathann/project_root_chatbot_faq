from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import data_preprocessing as dtp
import joblib

# Obter conjunto de dados pre-processado
def pre_processing():
    X_tfidf, y_encoded, vectorizer, label_encoder = dtp.load_and_prepare_data()
    return X_tfidf, y_encoded, vectorizer, label_encoder

# Dividindo conjunto de dados em treino e teste
def feature_model_training(X, y):
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, y_train

# Treinando modelo SVM
def training_model(X_train, y_train):
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)
    return model

def main():
    # Pre-processamento
    X_tfidf, y_encoded, vectorizer, label_encoder = pre_processing()

    # Conjunto de dados de treino
    X_train, _, y_train = feature_model_training(X_tfidf, y_encoded)

    # Treino
    model = training_model(X_train, y_train)
    
    # Salvando artefatos
    joblib.dump(model, 'models/svm_model.pkl')
    joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
    joblib.dump(label_encoder, 'models/label_encoder.pkl')

    print("Modelo treinado e artefatos salvos com sucesso.")

if __name__ == "__main__":
    # Execução do script
    main()
