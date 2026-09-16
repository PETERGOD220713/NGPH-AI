<!doctype html>
<html lang="vi"><head><script>window["__codeletBootstrap__"]=JSON.parse('{"A":"A","B":"20260916-03-7343f9b","C":{"Abril Fatface":"YACgEZbkUVE,0","Alfa Slab One":"YACgEYS9sJU,0","Anton":"YACgEcYqQ-A,0","Archivo":"YAHO2-t-jNE,0","Arial":"YAGyDvJ_4Ts,0","Bebas Neue":"YACgESME5ew,0","Bricolage Grotesque":"YAFyMcdwzpc,0","Canva Sans":"YAFLd8sKbwc,2","Caveat":"YALBs2ploWQ,0","Comic Sans MS":"YAHO2VMiyZo,0","Cormorant Garamond":"YAFdJhX-538,0","Courier New":"YAGzXiGs0_8,0","DM Sans":"YAD1aU3sLnI,0","DM Serif Display":"YAD1aYG82rc,0","Forum":"YACgEcnnqB4,0","Fraunces":"YAEul-FRQw4,0","Georgia":"YAGzXkO0pEM,0","Helvetica Neue":"YAFcf6CtJfI,0","Impact":"YAFcfnjI7Vk,0","Inter":"YAFdJvSyp_k,3","Iowan Old Style":"YAGNIFa8j9o,0","Jacques Francois":"YAHO2a5g66Q,0","JetBrains Mono":"YAFdJksXcAk,0","Libre Baskerville":"YACgEUFdPdA,0","Manrope":"YAHO2b2feC4,0","Merriweather":"YACgEXvHxxs,0","Montserrat":"YADLjI9qxTA,0","Nunito":"YACgEX8C5Gg,0","Oleo Script":"YACgEQQ14jI,0","Phantom Sans":"YAHO2E8Pb88,0","Playfair Display":"YACgEYmuCJE,0","Poppins":"YAFdJjbTu24,1","Press Start 2P":"YAFyGr-8pmQ,0","Quicksand":"YADWjpfPmdk,0","Raleway":"YACgEVg3xZg,0","Segoe UI":"YAHNdRD1Klw,0","Source Sans 3":"YAG4lO1Mj10,0","Spectral":"YAHO2rVUHIM,0","Times New Roman":"YAGzXW3gftg,0","Times":"YAGzXW3gftg,0","Ubuntu":"YACgERDU--Q,0","Work Sans":"YAGXhLOKv44,0","Yellowtail":"YACgEYG4kG4,0","ui-monospace":"YADlN8CFZ8Q,0","ui-sans-serif":"YACkoN-xg4g,0"}}');</script><script src="/_sdk/c21197326e9a1154.telemetry_sdk.js" integrity="sha512-Aqwl+NmLtKBcMQM4HY+W9lmBHa+zP5MqSEuYfCjkzt4xeOSv2xNz81cCp7JyXBVrY+zojg5o94FHY/R31v2d3Q=="></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NGPH AI</title>
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.577.0/dist/umd/lucide.min.js"></script>
  <script src="/_sdk/efe904fe8a212716.data_sdk.js" integrity="sha512-oiO0pmn5llS1uDeB2l690YywxqOe/a0U1kzY6RGaLZXtyh9YjTk1CUoK/bJUugc1QbUaJMJ3IE1MtpNY5NBZCw=="></script>
  <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <style>
    :root {
      --ink: #18252d;
      --muted: #66747d;
      --line: #dce5e4;
      --paper: #ffffff;
      --sage: #eaf3ef;
      --forest: #176b55;
      --forest-dark: #105441;
      --orange: #ec8557;
    }

    * { box-sizing: border-box; }

    body {
      width: 100%;
      min-height: 100%;
      margin: 0;
      font-family: "Work Sans", sans-serif;
      color: var(--ink);
    }

    .app-shell {
      width: 100%;
      min-height: calc(100 * min(var(--vh, 1vh), 1vh));
      position: relative;
      overflow: hidden;
      padding: 28px 16px;
    }

    .app-shell::before,
    .app-shell::after {
      content: "";
      position: absolute;
      width: 340px;
      height: 340px;
      border-radius: 999px;
      pointer-events: none;
      filter: blur(2px);
      opacity: 0.55;
    }

    .app-shell::before {
      top: -170px;
      left: -130px;
      background: #cfe6db;
    }

    .app-shell::after {
      right: -180px;
      bottom: -190px;
      background: #f8d8c7;
    }

    .chat-frame {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
      border: 1px solid rgba(24, 37, 45, 0.09);
      box-shadow: 0 25px 70px rgba(29, 57, 49, 0.15);
      border-radius: 28px;
      overflow: hidden;
    }

    .chat-scroll {
      min-height: 310px;
      max-height: calc(52 * min(var(--vh, 1vh), 1vh));
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: #b4c5bf transparent;
    }

    .message-row {
      display: flex;
      gap: 10px;
      align-items: flex-end;
      margin-bottom: 18px;
      animation: rise-in 260ms ease-out both;
    }

    .message-row.user {
      justify-content: flex-end;
    }

    .message-avatar {
      flex: 0 0 auto;
      width: 32px;
      height: 32px;
      border-radius: 12px;
      display: grid;
      place-items: center;
      color: #ffffff;
      background: var(--forest);
    }

    .message-avatar.user-avatar {
      background: #e6a274;
      color: #54311f;
    }

    .message-bubble {
      max-width: min(76%, 590px);
      padding: 12px 15px;
      border-radius: 18px;
      line-height: 1.55;
      font-size: 0.95rem;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
    }

    .assistant-bubble {
      color: #25353a;
      background: #edf5f2;
      border-bottom-left-radius: 5px;
    }

    .user-bubble {
      color: #ffffff;
      background: var(--forest);
      border-bottom-right-radius: 5px;
    }

    .message-time {
      font-size: 0.69rem;
      color: #819099;
      margin-top: 5px;
    }

    .typing-dots {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 12px 15px;
      border-radius: 18px;
      border-bottom-left-radius: 5px;
      background: #edf5f2;
    }

    .typing-dots span {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #628478;
      animation: bounce 1.1s infinite ease-in-out;
    }

    .typing-dots span:nth-child(2) { animation-delay: 120ms; }
    .typing-dots span:nth-child(3) { animation-delay: 240ms; }

    .suggestion-button {
      border: 1px solid #d8e4df;
      background: #ffffff;
      color: #355248;
      transition: transform 160ms ease, border-color 160ms ease, background 160ms ease;
    }

    .suggestion-button:hover {
      transform: translateY(-2px);
      border-color: #8eb6a6;
      background: #f3f8f6;
    }

    .suggestion-button:focus-visible,
    button:focus-visible,
    textarea:focus-visible {
      outline: 3px solid rgba(236, 133, 87, 0.42);
      outline-offset: 3px;
    }

    .send-action {
      transition: background 160ms ease, transform 160ms ease, opacity 160ms ease;
    }

    .send-action:hover:not(:disabled) {
      transform: translateY(-1px);
      background: var(--forest-dark);
    }

    .send-action:disabled {
      opacity: 0.58;
      cursor: not-allowed;
    }

    @keyframes rise-in {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes bounce {
      0%, 70%, 100% { transform: translateY(0); opacity: 0.5; }
      35% { transform: translateY(-4px); opacity: 1; }
    }

    @media (max-width: 640px) {
      .app-shell { padding: 12px; }
      .chat-frame { border-radius: 22px; }
      .chat-scroll { max-height: calc(49 * min(var(--vh, 1vh), 1vh)); }
      .message-bubble { max-width: 84%; }
    }
  </style>
  <script src="/_sdk/fab616ff82261ec3.resizing_sdk.js" type="text/javascript" integrity="sha512-6HMQCcUK6kDKuW59G/ZuFQDLjI3pOzz+2hgX6MaEV1izmYwYrrxv76nfirS4geYvvwnfUYWKbXBg/ycD2lR6jw=="></script>
 </head>
 <body data-template-id="__page-root" style="background: linear-gradient(135deg, rgb(241, 248, 244), rgb(255, 250, 246));">
  <div class="app-shell">
   <main class="w-full" aria-labelledby="app-title">
    <section class="chat-frame bg-white">
     <header data-template-id="chat-header" class="canva-header px-5 pt-6 pb-5 sm:px-8 sm:pt-8" style="background: rgb(255, 255, 255);">
      <div class="flex flex-col gap-5 sm:flex-row sm:items-start sm:justify-between">
       <div class="max-w-xl">
        <div data-template-id="demo-badge" class="canva-tag inline-flex rounded-full px-3 py-1 text-xs font-bold tracking-wide" style="background: rgb(234, 243, 239); color: rgb(23, 107, 85); font-weight: 700; font-style: normal; font-size: 12px; letter-spacing: 0.06rem;">BẢN DEMO • TIẾNG VIỆT</div>
        <h1 data-template-id="app-title" class="canva-text mt-3 font-extrabold tracking-tight" style="color: rgb(24, 37, 45); font-weight: 800; font-style: normal; font-size: 32px; letter-spacing: -0.04rem;">NGPH AI</h1>
        <p data-template-id="intro-copy" class="canva-text mt-2 leading-relaxed" style="color: rgb(102, 116, 125); font-weight: 400; font-style: normal; font-size: 16px; line-height: 1.5;">Chào bạn! Hãy đặt câu hỏi, lên ý tưởng hoặc bắt đầu một kế hoạch nhỏ cùng tôi.</p>
       </div>
       <div class="flex shrink-0 items-center gap-2">
        <button id="clear-trigger" data-template-id="clear-button" type="button" class="canva-button inline-flex items-center gap-2 rounded-xl px-3 py-2 text-sm font-semibold transition hover:opacity-80" style="background: rgb(255, 240, 233); color: rgb(166, 78, 45); font-weight: 600;"> <i data-lucide="trash-2" width="16" height="16" aria-hidden="true"></i> <span></span> </button>
       </div>
      </div>
      <div id="clear-confirmation" class="mt-4 hidden items-center justify-between gap-3 rounded-xl border border-orange-200 bg-orange-50 px-4 py-3">
       <p data-template-id="clear-confirm-copy" class="canva-text text-sm leading-snug" style="color: rgb(140, 72, 45); font-weight: 500; font-style: normal; font-size: 16px;">Bạn có chắc muốn xoá toàn bộ cuộc trò chuyện không?</p>
       <div class="flex shrink-0 gap-2">
        <button id="clear-cancel" data-template-id="clear-cancel-button" type="button" class="canva-button rounded-lg px-3 py-2 text-sm font-semibold" style="background: rgb(255, 255, 255); color: rgb(91, 101, 104); font-weight: 600; font-style: normal; font-size: 16px;">Huỷ</button> <button id="clear-confirm" data-template-id="clear-confirm-button" type="button" class="canva-button rounded-lg px-3 py-2 text-sm font-semibold" style="background: rgb(200, 93, 57); color: rgb(255, 255, 255); font-weight: 700; font-style: normal; font-size: 16px;">Xoá tất cả</button>
       </div>
      </div>
     </header>
     <section class="border-y border-[#e5ece9] bg-[#fbfdfc]">
      <div id="chat-history" class="chat-scroll px-5 py-6 sm:px-8" aria-live="polite" aria-label="Lịch sử trò chuyện">
       <div id="loading-state" class="flex min-h-[250px] flex-col items-center justify-center text-center">
        <div class="mb-3 h-8 w-8 animate-spin rounded-full border-[3px] border-[#c8ddd4] border-t-[#176b55]"></div>
        <p data-template-id="loading-copy" class="canva-text" style="color: rgb(102, 116, 125); font-weight: 400; font-style: normal; font-size: 15px;">Đang tải cuộc trò chuyện của bạn…</p>
       </div>
       <div id="empty-state" class="hidden min-h-[250px] flex-col items-center justify-center text-center">
        <div class="mb-4 grid h-14 w-14 place-items-center rounded-2xl bg-[#eaf3ef] text-[#176b55]">
         <i data-lucide="sparkles" width="27" height="27" aria-hidden="true"></i>
        </div>
        <h2 data-template-id="empty-title" class="canva-text font-bold" style="color: rgb(36, 53, 58); font-weight: 700; font-style: normal; font-size: 24px;">Bắt đầu cuộc trò chuyện</h2>
        <p data-template-id="empty-copy" class="canva-text mt-2 max-w-sm leading-relaxed" style="color: rgb(104, 122, 128); font-weight: 400; font-style: normal; font-size: 15px; line-height: 1.5;">Tôi sẽ đưa ra các gợi ý hữu ích dựa trên từ khoá. Đây là phiên bản demo, chưa kết nối mô hình AI bên ngoài.</p>
       </div>
       <div id="load-error-state" class="hidden min-h-[250px] flex-col items-center justify-center text-center">
        <div class="mb-4 grid h-14 w-14 place-items-center rounded-2xl bg-[#fff0e9] text-[#b75c38]">
         <i data-lucide="wifi-off" width="25" height="25" aria-hidden="true"></i>
        </div>
        <h2 data-template-id="load-error-title" class="canva-text font-bold" style="color: rgb(36, 53, 58); font-weight: 700; font-style: normal; font-size: 24px;">Chưa thể tải cuộc trò chuyện</h2>
        <p data-template-id="load-error-copy" class="canva-text mt-2 max-w-sm leading-relaxed" style="color: rgb(104, 122, 128); font-weight: 400; font-style: normal; font-size: 15px; line-height: 1.5;">Vui lòng kiểm tra lại kết nối rồi thử tải lại lịch sử trò chuyện.</p><button id="retry-load" data-template-id="retry-button" type="button" class="canva-button mt-4 rounded-xl px-4 py-2 text-sm font-semibold" style="background: rgb(23, 107, 85); color: rgb(255, 255, 255); font-weight: 700; font-style: normal; font-size: 16px;">Thử lại</button>
       </div>
       <div id="messages-list" class="hidden"></div>
       <div id="typing-state" class="hidden mt-2">
        <div class="message-row">
         <div class="message-avatar">
          <i data-lucide="sparkles" width="16" height="16" aria-hidden="true"></i>
         </div>
         <div>
          <div class="typing-dots" aria-label="Trợ lý đang trả lời">
           <span></span><span></span><span></span>
          </div>
          <p id="typing-label" class="mt-1 text-xs text-[#71827b]"></p>
         </div>
        </div>
       </div>
      </div>
     </section>
     <section class="px-5 pt-5 sm:px-8">
      <h2 data-template-id="suggestions-title" class="canva-text text-sm font-bold" style="color: rgb(61, 81, 76); font-weight: 700; font-style: normal; font-size: 14px;">Thử một câu hỏi mẫu</h2>
      <div class="mt-3 flex flex-wrap gap-2">
       <button data-template-id="suggestion-one" type="button" class="canva-button suggestion-button rounded-xl px-3 py-2 text-sm" style="color: rgb(53, 82, 72); font-weight: 400; font-style: normal; font-size: 14px;">Lên kế hoạch cho hôm nay</button> <button data-template-id="suggestion-two" type="button" class="canva-button suggestion-button rounded-xl px-3 py-2 text-sm" style="color: rgb(53, 82, 72); font-weight: 400; font-style: normal; font-size: 14px;">Gợi ý ý tưởng nội dung</button> <button data-template-id="suggestion-three" type="button" class="canva-button suggestion-button rounded-xl px-3 py-2 text-sm" style="color: rgb(53, 82, 72); font-weight: 400; font-style: normal; font-size: 14px;">Giúp tôi học hiệu quả hơn</button> <button data-template-id="suggestion-four" type="button" class="canva-button suggestion-button rounded-xl px-3 py-2 text-sm" style="color: rgb(53, 82, 72); font-weight: 400; font-style: normal; font-size: 14px;">Cách viết một caption ngắn?</button>
      </div>
     </section>
     <footer class="px-5 pb-5 pt-5 sm:px-8 sm:pb-7">
      <form id="message-form" class="rounded-2xl border border-[#cedbd6] bg-white p-2 shadow-sm">
       <label data-template-id="message-label" for="message-input" class="canva-text sr-only" style="font-weight: 400; font-style: normal; font-size: 16px;">Nhập tin nhắn cho NGPH AI</label> <textarea id="message-input" rows="2" maxlength="1000" class="w-full resize-none border-0 bg-transparent px-3 py-2 text-[15px] leading-relaxed text-[#1c2b30] placeholder:text-[#91a09c] focus:outline-none" placeholder="Nhập tin nhắn..."></textarea>
       <div class="flex items-center justify-between gap-3 px-1 pb-1">
        <p data-template-id="enter-hint" class="canva-text text-xs" style="color: rgb(124, 139, 135); font-weight: 400; font-style: normal; font-size: 12px;">Enter để gửi · Shift + Enter xuống dòng</p><button id="send-button" data-template-id="send-button" type="submit" class="canva-button send-action inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-bold" style="background: rgb(23, 107, 85); color: rgb(255, 255, 255); font-weight: 700;"> <i data-lucide="send" width="16" height="16" aria-hidden="true"></i> <span></span> </button>
       </div>
      </form>
      <p id="action-status" class="mt-3 min-h-5 text-center text-xs text-[#71827b]" role="status"></p>
     </footer>
    </section>
   </main>
  </div>
  <template id="message-template">
   <article class="message-row">
    <div class="message-avatar">
     <i data-lucide="sparkles" width="16" height="16" aria-hidden="true"></i>
    </div>
    <div>
     <div class="message-bubble"></div>
     <p class="message-time"></p>
    </div>
   </article>
  </template>
  <script src="/_sdk/d80b7fc77c36e544.editing_sdk.js" integrity="sha512-G1c7mLHfqSpyYPFnCMpb8X52/iP9EEJ4y/O8pmYPhWe33R+uuxRRWVYdXU2F+N4m0Y2/2lhbJGfxoPXkVhIZzw=="></script>
  <script>
    let backendRecords = [];
    let initialLoadTimer;
    let isInitialLoadComplete = false;
    let writeChain = Promise.resolve();
    let lastWriteAt = 0;

    const historyEl = document.getElementById("chat-history");
    const listEl = document.getElementById("messages-list");
    const loadingEl = document.getElementById("loading-state");
    const emptyEl = document.getElementById("empty-state");
    const errorEl = document.getElementById("load-error-state");
    const typingEl = document.getElementById("typing-state");
    const inputEl = document.getElementById("message-input");
    const formEl = document.getElementById("message-form");
    const sendButton = document.getElementById("send-button");
    const statusEl = document.getElementById("action-status");
    const confirmationEl = document.getElementById("clear-confirmation");
    const clearTrigger = document.getElementById("clear-trigger");
    const typingLabel = document.getElementById("typing-label");

    typingLabel.textContent = "Trợ lý đang soạn phản hồi…";

    function setStatus(message, type) {
      statusEl.textContent = message;
      statusEl.className = "mt-3 min-h-5 text-center text-xs " + (type === "error" ? "text-[#b35032]" : "text-[#4e7567]");
    }

    function setLoadingView() {
      loadingEl.classList.remove("hidden");
      loadingEl.classList.add("flex");
      emptyEl.classList.add("hidden");
      emptyEl.classList.remove("flex");
      errorEl.classList.add("hidden");
      errorEl.classList.remove("flex");
      listEl.classList.add("hidden");
    }

    function showLoadError() {
      loadingEl.classList.add("hidden");
      loadingEl.classList.remove("flex");
      emptyEl.classList.add("hidden");
      emptyEl.classList.remove("flex");
      listEl.classList.add("hidden");
      errorEl.classList.remove("hidden");
      errorEl.classList.add("flex");
    }

    function formatTime(iso) {
      const date = new Date(iso);
      if (Number.isNaN(date.getTime())) return "";
      return new Intl.DateTimeFormat("vi-VN", {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "2-digit"
      }).format(date);
    }

    function sortedRecords(records) {
      return [...records].sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
    }

    function render(records) {
      loadingEl.classList.add("hidden");
      loadingEl.classList.remove("flex");
      errorEl.classList.add("hidden");
      errorEl.classList.remove("flex");

      if (!records.length) {
        listEl.classList.add("hidden");
        emptyEl.classList.remove("hidden");
        emptyEl.classList.add("flex");
        return;
      }

      emptyEl.classList.add("hidden");
      emptyEl.classList.remove("flex");
      listEl.classList.remove("hidden");

      const existing = new Map([...listEl.children].map((node) => [node.dataset.recordId, node]));
      const fragment = document.createDocumentFragment();

      sortedRecords(records).forEach((record) => {
        let row = existing.get(record.__backendId);

        if (!row) {
          const clone = document.getElementById("message-template").content.cloneNode(true);
          row = clone.querySelector("article");
          row.dataset.recordId = record.__backendId;
          fragment.appendChild(row);
          lucide.createIcons();
        }

        const isUser = record.role === "user";
        row.classList.toggle("user", isUser);

        const avatar = row.querySelector(".message-avatar");
        avatar.classList.toggle("user-avatar", isUser);
        avatar.innerHTML = isUser
          ? '<i data-lucide="user" width="16" height="16" aria-hidden="true"></i>'
          : '<i data-lucide="sparkles" width="16" height="16" aria-hidden="true"></i>';

        const bubble = row.querySelector(".message-bubble");
        bubble.classList.toggle("user-bubble", isUser);
        bubble.classList.toggle("assistant-bubble", !isUser);
        bubble.textContent = record.content;
        row.querySelector(".message-time").textContent = formatTime(record.created_at);

        existing.delete(record.__backendId);
        if (!row.parentElement) fragment.appendChild(row);
      });

      existing.forEach((node) => node.remove());
      if (fragment.childNodes.length) listEl.appendChild(fragment);
      lucide.createIcons();
    }

    function scrollToLatest() {
      requestAnimationFrame(() => {
        historyEl.scrollTop = historyEl.scrollHeight;
      });
    }

    function makeDemoReply(message) {
      const value = message.toLowerCase().trim();

      if (/(ai là người tạo|ai phát triển|người phát triển|tác giả|người tạo ra|developer|author)/.test(value)) {
        return "Người tạo ra NGPH AI là Bùi Tấn Nghĩa, hiện đang học tại Trường THCS Nguyễn Hiền.";
      }
      if (/(xin chào|chào|hello|hi)/.test(value)) {
        return "Xin chào! Tôi là Trợ lý AI bản demo. Tôi có thể giúp bạn phác thảo ý tưởng, lập kế hoạch và viết nội dung ngắn bằng tiếng Việt.";
      }
      if (/(kế hoạch|lập kế hoạch|plan|mục tiêu)/.test(value)) {
        return "Đây là gợi ý từ bản demo: hãy bắt đầu bằng 1 mục tiêu cụ thể, chia thành 3 việc quan trọng nhất, rồi dành một khung thời gian ngắn cho từng việc. Bạn muốn lập kế hoạch cho ngày, tuần hay một dự án?";
      }
      if (/(viết|nội dung|bài đăng|caption|email)/.test(value)) {
        return "Bản demo gợi ý cấu trúc viết nhanh: mở đầu bằng lợi ích rõ ràng, thêm 2–3 ý chính dễ quét, rồi kết thúc bằng một lời kêu gọi hành động. Hãy cho tôi biết chủ đề và đối tượng bạn muốn hướng đến.";
      }
      if (/(học|ôn tập|kiến thức|tiếng anh|bài tập)/.test(value)) {
        return "Bản demo đề xuất bạn học theo vòng ngắn: chọn một chủ đề, học tập trung 25 phút, tự tóm tắt 3 ý, rồi nghỉ 5 phút. Tôi cũng có thể giúp bạn tạo dàn ý ôn tập nếu bạn nêu môn học.";
      }
      if (/(ý tưởng|sáng tạo|brainstorm)/.test(value)) {
        return "Bản demo đây: hãy thử nhìn vấn đề từ 3 góc độ — người dùng cần gì, điều gì khiến họ bất ngờ, và giải pháp tối giản nhất là gì. Bạn có thể nói thêm chủ đề để tôi gợi ý cụ thể hơn.";
      }
      if (/(tóm tắt|tóm lược)/.test(value)) {
        return "Tôi là bản demo nên chưa thể đọc tài liệu bên ngoài. Bạn có thể dán đoạn văn cần tóm tắt vào đây, và tôi sẽ giúp bạn rút ra các ý chính.";
      }
      return "Cảm ơn bạn đã nhắn! Đây là phản hồi từ Trợ lý AI bản demo, hiện chưa kết nối mô hình AI bên ngoài. Hãy cho tôi thêm bối cảnh hoặc mục tiêu cụ thể để tôi gợi ý hữu ích hơn.";
    }

    function queueWrite(task) {
      writeChain = writeChain.then(async () => {
        const wait = Math.max(0, 550 - (Date.now() - lastWriteAt));
        if (wait) await new Promise((resolve) => setTimeout(resolve, wait));
        const result = await task();
        lastWriteAt = Date.now();
        return result;
      });
      return writeChain;
    }

    async function createMessage(record) {
      if (backendRecords.length >= 999) {
        setStatus("Cuộc trò chuyện đã đạt giới hạn 999 tin nhắn.", "error");
        return false;
      }

      const result = await queueWrite(() => window.dataSdk.create(record));
      if (!result.isOk) {
        setStatus("Không thể xác nhận lưu tin nhắn. Vui lòng thử lại sau.", "error");
        return false;
      }
      return true;
    }

    async function sendMessage(text, control) {
      const content = text.trim();
      if (!content) {
        inputEl.focus();
        return;
      }

      control.disabled = true;
      inputEl.value = "";
      typingEl.classList.remove("hidden");
      setStatus("", "success");
      scrollToLatest();

      try {
        const userSaved = await createMessage({
          role: "user",
          content,
          created_at: new Date().toISOString()
        });

        if (!userSaved) return;

        await new Promise((resolve) => setTimeout(resolve, 450));

        const assistantSaved = await createMessage({
          role: "assistant",
          content: makeDemoReply(content),
          created_at: new Date().toISOString()
        });

        if (assistantSaved) setStatus("Phản hồi demo đã được lưu vào cuộc trò chuyện.", "success");
      } finally {
        typingEl.classList.add("hidden");
        control.disabled = false;
        inputEl.focus();
        scrollToLatest();
      }
    }

    const handler = {
      onDataChanged(data) {
        clearTimeout(initialLoadTimer);
        isInitialLoadComplete = true;
        backendRecords = data;
        render(data);
        scrollToLatest();
      }
    };

    async function initializeDataSdk() {
      clearTimeout(initialLoadTimer);
      if (!isInitialLoadComplete) setLoadingView();

      initialLoadTimer = setTimeout(() => {
        if (!isInitialLoadComplete) showLoadError();
      }, 8000);

      const initResult = await window.dataSdk.init(handler);
      if (!initResult.isOk) {
        clearTimeout(initialLoadTimer);
        showLoadError();
      }
    }

    formEl.addEventListener("submit", (event) => {
      event.preventDefault();
      sendMessage(inputEl.value, event.submitter || sendButton);
    });

    inputEl.addEventListener("keydown", (event) => {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        formEl.requestSubmit(sendButton);
      }
    });

    document.querySelectorAll(".suggestion-button").forEach((button) => {
      button.addEventListener("click", () => {
        const suggestion = button.textContent.trim();
        if (!suggestion) return;
        inputEl.value = suggestion;
        formEl.requestSubmit(sendButton);
      });
    });

    clearTrigger.addEventListener("click", () => {
      confirmationEl.classList.remove("hidden");
      confirmationEl.classList.add("flex");
    });

    document.getElementById("clear-cancel").addEventListener("click", () => {
      confirmationEl.classList.add("hidden");
      confirmationEl.classList.remove("flex");
    });

    document.getElementById("clear-confirm").addEventListener("click", async (event) => {
      const button = event.currentTarget;
      const recordsToDelete = [...backendRecords];

      if (!recordsToDelete.length) {
        confirmationEl.classList.add("hidden");
        confirmationEl.classList.remove("flex");
        setStatus("Chưa có tin nhắn để xoá.", "success");
        return;
      }

      button.disabled = true;
      setStatus("Đang xoá cuộc trò chuyện…", "success");

      try {
        for (const record of recordsToDelete) {
          const result = await queueWrite(() => window.dataSdk.delete(record));
          if (!result.isOk) {
            setStatus("Không thể xác nhận xoá toàn bộ lịch sử. Vui lòng thử lại.", "error");
            return;
          }
        }
        setStatus("Đã xoá cuộc trò chuyện.", "success");
        confirmationEl.classList.add("hidden");
        confirmationEl.classList.remove("flex");
      } finally {
        button.disabled = false;
      }
    });

    document.getElementById("retry-load").addEventListener("click", () => {
      isInitialLoadComplete = false;
      initializeDataSdk();
    });

    document.addEventListener("DOMContentLoaded", () => {
      lucide.createIcons();
      initializeDataSdk();
    });
  </script>
 
</body></html>
