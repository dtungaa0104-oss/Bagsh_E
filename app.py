from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load curriculum data
with open('data/curriculum.json', 'r', encoding='utf-8') as f:
    CURRICULUM = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', 
                           grades=CURRICULUM['grades'],
                           periods=CURRICULUM['periods'])

@app.route('/api/subjects/<grade>')
def get_subjects(grade):
    grade_data = CURRICULUM['grades'].get(grade, {})
    subjects = list(grade_data.get('subjects', {}).keys())
    return jsonify(subjects)

@app.route('/api/topics/<grade>/<subject>')
def get_topics(grade, subject):
    grade_data = CURRICULUM['grades'].get(grade, {})
    subjects = grade_data.get('subjects', {})
    topics = subjects.get(subject, {}).get('topics', [])
    return jsonify(topics)

@app.route('/api/generate', methods=['POST'])
def generate_plan():
    data = request.json
    
    manager_name = data.get('manager_name', '')
    subject = data.get('subject', '')
    topic = data.get('topic', '')
    grade = data.get('grade', '')
    period = data.get('period', '40')
    objectives = data.get('objectives', '')
    teacher_name = data.get('teacher_name', '')
    
    grade_label = CURRICULUM['grades'].get(grade, {}).get('label', f'{grade}-р анги')
    
    plan = generate_lesson_plan(
        manager_name=manager_name,
        teacher_name=teacher_name,
        subject=subject,
        topic=topic,
        grade_label=grade_label,
        period=period,
        objectives=objectives
    )
    
    return jsonify({'plan': plan})

def generate_lesson_plan(manager_name, teacher_name, subject, topic, grade_label, period, objectives):
    period_int = int(period)
    
    # Calculate time allocations
    intro_time = max(5, period_int // 8)
    explore_time = period_int // 3
    practice_time = period_int // 4
    elaborate_time = period_int // 6
    evaluate_time = period_int - intro_time - explore_time - practice_time - elaborate_time
    
    plan = {
        'header': {
            'subject': subject,
            'topic': topic,
            'grade': grade_label,
            'period': f'{period} минут',
            'manager': manager_name,
            'teacher': teacher_name
        },
        'objectives': {
            'A': f'Сурагч {topic}-ийн үндсэн ойлголт, тодорхойлолтыг мэдэж, хэрэглэх чадвартай болно.',
            'B': f'Сурагч {topic}-ийг өмнөх мэдлэгтэй холбон тайлбарлах, жишээ гаргаж чадна.',
            'C': f'Сурагч {topic}-ийн мэдлэгийг өөрийн амьдралд хэрэглэж, бүтээлч даалгавар гүйцэтгэх чадвартай болно.'
        },
        'design': {
            'method': 'Судалгаанд суурилсан индуктив арга (Discovery Learning): сурагч жишээ дүн шинжилгээгээр дүгнэлт гаргана. Бүлгийн хамтарсан суралцахуйг (Cooperative Learning) хос болон бүлгээр ажиллуулж, харилцан тайлбарлуулна.',
            'tools': f'Wordwall.net тааламжтай интерактив дасгал; Jamboard эсвэл Padlet: сурагч бүлгээр үзэл бодлоо картаар харуулна. Хэлхэмж зургийн карт: ирэхдийн хувьд {topic} харилцааг харуулна.',
            'engagement': f'Нийт 30 сурагч Engage болон Explore үе шатанд ширээний бүлгээр ажиллана. 4-5 унийн бүлгээр ажиллана. Сурагчдын хоёр ширээний байрлал анги зохиомжид тохируулан өмнөх хичээлийн баталгаасны дараа болно.'
        },
        'stages': [
            {
                'name': 'I. ЭХЛЭЛ',
                'time': intro_time,
                'purpose': f'Оролцоо ба идэвхжүүлэлт',
                'teacher_actions': f'Монгол 2050 оны хэтийн төлөвт холбогдох нээлттэй асуулт тавина. Мэдлэгийн зураглал нөхлөтэй ашиглан урьдчилсан мэдлэгийг идэвхжүүлнэ.',
                'student_actions': f'Сурагчид {topic}-тай холбоотой өөрсдийн мэдлэг, туршлагаа хуваалцана. Анхны санаа бодлоо илэрхийлнэ.',
                'assessment': 'Асуулт хариулт, харилцан ярилцалт'
            },
            {
                'name': 'II. ОРОЛЦОЛ',
                'time': explore_time,
                'purpose': 'Шинэ мэдлэг олж авах',
                'teacher_actions': f'Алхам 1 – Explore ({min(8, explore_time//3)} мин): Бүлг дүрмийн тухай асуулт тавьж, {topic}-ийн жишээнүүдийг судлуулна.\nАлхам 2 – Explain ({min(7, explore_time//3)} мин): Бүлгүүдийн олсон дүрмийг нэгтгэн баталгаажуулна. Subject + verb (infinitive) бүтцийг дэлгэрэнгүй тайлбарлана.\nАлхам 3 – Guided Practice ({min(10, explore_time//2)} мин): Wordwall.net дээр баталгаажуулах Match and Fill дасгалыг бүлгээр компьютерт хийнэ. Хэлхэмж картаар зохиомж зохионо.',
                'student_actions': f'Хос болон бүлгээр ажиллан Монгол хэлэнд аймаар зөв хариулт ав-аж ахиулна. Сурагч {topic}-ийн жишээ тааруулж, бичиж, харилцана.',
                'assessment': 'Бүлгийн танилцуулга, Wordwall тохируулга'
            },
            {
                'name': 'III. ДҮГНЭЛТ',
                'time': evaluate_time,
                'purpose': 'Ойлголт бататгал, үнэлгээ',
                'teacher_actions': f'Тухайн хичээлийн үр дүнг дүгнэн, дараагийн хичээлийн холбоог тодорхойлно. Гэрийн даалгавар өгнө.',
                'student_actions': f'Хичээлээс юу сурснаа 3-2-1 аргаар тэмдэглэнэ (3 зүйл сурсан, 2 сонирхолтой, 1 асуулт). Exit ticket бөглөнө.',
                'assessment': '3-2-1 карт, Exit ticket үнэлгээ'
            }
        ],
        'differentiation': {
            'support': f'Дэмжлэг хэрэгтэй сурагчид: {topic}-ийн хялбаршуулсан жишээ, нөхөх дасгал, хос ажил',
            'advanced': f'Дэвшилтэт сурагчид: {topic}-ийг ахисан түвшний даалгавар, бүтээлч хэрэглээний жишээ гаргах, бусдад тайлбарлах'
        },
        'homework': f'{topic}-тай холбоотой 5-7 жишээ бичиж, ямар нөхцөл байдалд хэрэглэгддэгийг тайлбарлах'
    }
    
    return plan

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
