chain_type


LangChain还提供了其他几种处理文档块的方式，例如：

stuff:将所有检索到的文档块简单地拼接在一起，形成一个长的文本，然后将这个拼接后的文本作为上下文与用户的问题一起传递给大语言模型（LLM），LLM根据这个上下文生成答

‌map_reduce‌：将每个文档块分别传递给LLM生成部分答案，然后将所有部分答案汇总成一个最终答案。适合处理大量文档块，避免输入长度限制‌
 
‌refine‌：对每个文档块进行细化处理后再传递给LLM。适用于需要精细处理的场景‌
 
‌map_rerank‌：对检索到的文档块进行重新排序后再传递给LLM。适用于需要优化排序结果的场景‌
 

retriever = vector_store.as_retriever( search_type="similarity")

search_type可选 "similarity"|"mmr"|"similarity_score_threshold"

•mmr-最大边际相关性
原理：在相似度的基础上增加多样性控制，避免返回内容重复的结果
核心参数：
◦lambda_mult：0-1之间的值，越小结果越多样
▪接近1：更偏向相似度（类似similarity）
▪接近0：更偏向多样性

similarity_score_threshold-带分数阈值的相似度搜索
•原理：只返回相似度超过设定阈值的文档
•关键参数：
◦score_threshold：相似度阈值（余弦相似度范围0-1）
◦k：最大返回数量（但实际数量可能少于k）
•特点：
◦适合质量优先的场景
◦结果数量不固定（可能返回0个或多个）
