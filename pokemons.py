import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)
# CSS 이용해서 Styling하기
st.markdown(
    """
    <style>
    img { max-height: 200px; }
    
    </style>
    """, unsafe_allow_html=True)

st.title("Streamlit :red[포켓몬] 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

# session_state에 포켓몬 리스트 저장하기
# pokemons --> initial_pokemons 변경
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]



if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

# toggle 기능
auto_complete = st.toggle("예시 데이터로 채우기", value=False, key="auto_complete")

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

# 포켓몬 이미지 추가하기 
with st.form (key="pokemon_form"):
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else "", 
            )
    with col2:
        types = st.multiselect(label="포켓몬 타입", 
                            options=list(type_emoji_dict.keys()),
                            max_selections=2,
                            default=example_pokemon["types"] if auto_complete else [],
        )    
    image_url = st.text_input(label="포켓몬 이미지 URL", 
                              value=example_pokemon["image_url"] if auto_complete else "",
                              placeholder="https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp"
    )
    
    submit_button = st.form_submit_button(label="포켓몬 추가")
    if submit_button:
        if not name : 
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 타입을 1개 이상 선택해주세요.")
        else:
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })
            st.success(f"'{name}' 포켓몬이 추가되었습니다.")

# --------------------------------------------------
cols = st.columns(3)
for i in range(len(st.session_state.pokemons)):
    with cols[i % 3]:
        pokemon = st.session_state.pokemons[i]
        with st.expander(label=f'**{i+1}. {str(pokemon["name"])}**', expanded=True):
            st.image(pokemon["image_url"])
            emoji_types = [f"{type_emoji_dict[x]}{x}" for x in pokemon["types"]]
            st.text(" / ".join(emoji_types))
            
            # 삭제하는 버튼 추가하기
            if st.button("삭제", key=f"delete_{i}"):
                del st.session_state.pokemons[i]
                st.rerun()


