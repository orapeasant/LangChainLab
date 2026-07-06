from langchain_community.embeddings import DashScopeEmbeddings
#DashScopeEmbeddings
#阿里巴巴的包
#专门用来调用阿里云上的各类模型服务
#初始化Dashscope Embeddings
embeddings =DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key="sk-6790bcf8821e466bb015d5d297c413d4",
)
vector1=embeddings.embed_query("你好")
print (len(vector1))


vector2=embeddings.embed_query("小说写一个人、几个人、一群人、或成千成万人的性格和感情。他们的性格和感情从横面的环境中反映出来，从纵面的遭遇中反映出来，从人与人之间的交往与关系中反映出来。长篇小说中似乎只有《鲁滨逊飘流记》，才只写一个人，写他与自然之间的关系，但写到后来，终于也出现了一个仆人“星期五”。只写一个人的短篇小说多些，尤其是近代与现代的新小说，写一个人在与环境的接触中表现他外在的世界、内心的世界，尤其是内心世界。有些小说写动物、神仙、鬼怪、妖魔，但也把他们当作人来写")
print (len(vector2))