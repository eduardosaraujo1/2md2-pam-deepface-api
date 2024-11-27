from deepface import DeepFace

def analyze_deepface(img):
    try:
        analysis = DeepFace.analyze(img_path=img, actions=["emotion"], enforce_detection=False)
        valid = validate_analysis(analysis)
        if valid:
            return analysis
        return None
    except Exception as e:
        log_analysis_error(e)
        return None

def validate_analysis(analysis):
    # Validar analise: é uma lista não vazia
    if not(isinstance(analysis, list) and len(analysis) > 0):
        log_analysis_error('DeepFace analysis returned an invalid list' )
        return False

    # Validar analise: item dentro da lista é valido
    for item in analysis:
        if not(isinstance(item, dict) and 'emotion' in item and 'dominant_emotion' in item):
            log_analysis_error('DeepFace analysis returned an invalid object')
            return False

    return True

def log_analysis_error(error):
    # TODO: Melhorar sistema de logging
    print(error)

def transform_scores(scores):
    return {key: round(scores[key].item(), 6) for key in scores.keys()}

def extract_analysis(analysis):
    """
    Estrutura anlálise da DeepFace em dados úteis
    """
    result = []
    for item in analysis:
        emotion = item['dominant_emotion']
        scores = transform_scores(item['emotion'])
        confidence = scores[emotion]
        result.append({
            'emotion': emotion,
            'confidence': confidence,
            'scores': scores
        })
    return result


def analyze(img):
    analysis = analyze_deepface(img)
    if not analysis:
        return None
    
    return extract_analysis(analysis)