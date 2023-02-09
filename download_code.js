// https://gist.github.com/XYShaoKang/1894a97bd2896d402f7bba6712cad72a

{
  void (async function main() {
    // 配置需要获取的题目索引,从 1 开始,想要获取哪题就添加哪一题的索引
    // 比如只想获取第三题和第四题,那就写 [3,4],要获取全部题目的提交的话,就写 [1,2,3,4]
    const questions = [1, 2, 3, 4]
    // 需要获取的页数,指定要获取哪几页的
    // 可以是数字,或者是用一个数组表示的区间,如 [3,6] 表示从 3 页到第 6 页
    const pages = [1]
    // 需要获取的竞赛 ID,可以通过每个比赛的链接处获取
    // 比如 https://leetcode-cn.com/contest/biweekly-contest-68/ 这是第 68 场双周赛的链接,其中 biweekly-contest-68 就是需要的部分
    const contestId = 'biweekly-contest-91'
    // 如果只获取国服的数据填 local,如果要获取全球的数据填 global
    const region = 'local'
    // 指定要获取的语言
    // 如果要获取所有语言,在数组中包含星号`*`
    // 如果只要获取某几种语言的,则去掉星号`*`,填入要获取的语言,比如['java','cpp']
    const lang = ['*']

    let res = `# ${contestId}\n`
    try {
      for (const page of pages) {
        if (Array.isArray(page)) {
          for (let i = page[0]; i <= page[1]; i++) {
            res += await getContest(lang, region, questions, contestId, i)
          }
        } else {
          res += await getContest(lang, region, questions, contestId, page)
        }
      }
      download(res, `${contestId}.md`)
    } catch (error) {
      console.log(error.message)
      download(res, `${contestId} - 目前已完成部分.md`)
    }
  })()

  /**
   *
   * @param data_region 所属的地区,"CN"或者"US"
   * @param submissionId 提交id
   * @returns {{code:string,contest_submission:number,id:number,lang:string}}
   */
  function getCode(data_region, submissionId, retry = 1) {
    const regionApi = data_region === 'CN' ? 'leetcode.cn' : 'leetcode.com'
    return fetch(`https://${regionApi}/api/submissions/${submissionId}/`, {
      headers: {
        'content-type': 'application/json',
      },
      referrer: 'https://leetcode.cn/contest/',
      referrerPolicy: 'strict-origin-when-cross-origin',
      body: null,
      method: 'GET',
      mode: 'cors',
      credentials: 'omit',
    }).then((res) => {
      if (res.status === 429) {
        console.log(`超出接口限制,休息一下,等待第${retry}次重试...`)
        if (retry > 5) {
          throw new Error(
            '已重试 5 次,仍然无法获取,可能力扣君生气了,晚点在试试吧...'
          )
        }
        // 请求太频繁的限制
        return sleep(3000).then(() =>
          getCode(data_region, submissionId, retry + 1)
        )
      }
      return res.json()
    })
  }

  /**
   * 获取比赛的数据
   * @param region 所属的地区: 国服:"local";外服:"global"
   * @param contestId 比赛Id
   * @param page 页数
   * @returns {{
   *    is_past: boolean
   *    submissions: {
   *      [submissionId:string]:{
   *        id: number
   *        date: number
   *        question_id: number
   *        submission_id: number
   *        status: number
   *        contest_id: number
   *        data_region: string
   *        fail_count: number
   *        lang: string
   *      }
   *    }[]
   *    questions: {
   *      id: number
   *      question_id: number
   *      credit: number
   *      title: string
   *      english_title: string
   *      title_slug: string
   *      category_slug: string
   *    }[]
   *    total_rank:{
   *      contest_id: number
   *      username: string
   *      user_slug: string
   *      real_name: string
   *      country_code: string
   *      country_name: string
   *      rank: number
   *      score: number
   *      finish_time: number
   *      global_ranking: number
   *      data_region: string
   *      avatar_url: string
   *      rank_v2: number
   *    }[]
   *    user_num: number
   * }}
   */
  function getRankData(region = 'local', contestId, page = 1) {
    if (region !== 'local' && region !== 'global') region = 'local'

    return fetch(
      `https://leetcode.cn/contest/api/ranking/${contestId}/?pagination=${page}&region=${region}`,
      {
        headers: {
          'content-type': 'application/json',
        },
        referrer: 'https://leetcode.cn/contest/',
        referrerPolicy: 'strict-origin-when-cross-origin',
        body: null,
        method: 'GET',
        mode: 'cors',
        credentials: 'omit',
      }
    ).then((res) => res.json())
  }

  /**
   * 创建文件下载
   * @param str 需要下载的内容
   * @param filename 文件名
   */
  function download(str, filename = 'contest.md') {
    const blob = new Blob([str], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)

    const a = document.createElement('a')
    a.href = url
    a.download = filename
    document.body.appendChild(a)
    a.click()

    document.body.removeChild(a)
  }

  function sleep(time) {
    return new Promise(function (resolve, reject) {
      setTimeout(resolve, time)
    })
  }

  async function getContest(lang, region, questionsArr, contestId, page) {
    lang = new Set(lang)
    console.log(`正在下载第 ${page} 页`)
    const questionSelect = new Set(questionsArr)
    const { submissions, total_rank, questions } = await getRankData(
      region,
      contestId,
      page
    )
    const questionIds = questions.map(({ question_id }) => question_id)

    let res = ''
    for (let i = 0; i < submissions.length; i++) {
      const { username, real_name } = total_rank[i]
      res += `\n## ${real_name || username}\n`

      const submission = submissions[i]

      for (let j = 0; j < questionIds.length; j++) {
        if (!questionSelect.has(j + 1)) continue

        const questionId = questionIds[j]

        if (!submission[questionId]) {
          res += '\n无\n\n'
          continue
        }

        const { submission_id, data_region } = submission[questionId]

        const code = await getCode(data_region, submission_id)
        console.log(code.lang)
        if (lang.has('*') || lang.has(code.lang)) {
          res += `
### 第${j + 1}题

\`\`\`${code.lang}
${code.code}
\`\`\`
`
        } else {
          // res += `\n### 第${j + 1}题\n\n该题代码语言为\`${
          //   code.lang
          // }\`,不在需要的语言类型中\n`
        }
      }
      // await sleep(100)
    }
    return res
  }
}