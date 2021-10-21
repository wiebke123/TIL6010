import streamlit as st
import plotly.express as px
    
df = px.data.gapminder()

st.title('Lets build an app in streamlit')
st.markdown("""
 * Gapminder data from plotly
 * Dropdown sidebar for the year
 * Your plots will appear below
""")

years = df['year'].unique()
df_years = df.groupby(["year", "continent"]).sum().reset_index()

chosen_year = st.sidebar.slider('Select a year', min_value=1952, max_value=2007, step=5)

if chosen_year:
    data_year = df.query("year=="+str(chosen_year))
    fig = px.scatter(data_year, x="gdpPercap", y="lifeExp",
               size="pop", color="continent", hover_name="country",
               log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    fig["layout"].pop("updatemenus") 
    st.title('Bubble Chart')
    st.plotly_chart(fig)
    
    data_year2 = df_years.query("year=="+str(chosen_year))
    fig2 = px.bar(data_year2, x="pop", y="continent", orientation='h', color="continent")
    fig2.update_layout(showlegend=False, xaxis_range=[0,4000000000])
    fig2.update_layout(yaxis={'categoryorder':'total ascending'})
    st.title('Bar Plot')
    st.plotly_chart(fig2)
