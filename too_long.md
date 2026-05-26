(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && find . \( -path './data' -o -path './node_modules' -o -path './.next' \) -prune -o -iname 'chat.tsx' -print
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && grep -RniE "fetch\\(|axios|WebSocket|EventSource|/api/|allis|chat|message|sendMessage|handleSubmit" . --include="*.tsx" --include="*.ts" --include="*.js" --include="*.jsx" --exclude-dir=data --exclude-dir=node_modules --exclude-dir=.next | head -n 250
./ms-allis-auth-install/frontend/app/setup-password/page.tsx:31:      setError(err.message || 'Could not set password');
./ms-allis-auth-install/frontend/app/login/page.tsx:11:  const [message, setMessage] = useState('Verifying your link…');
./ms-allis-auth-install/frontend/app/login/page.tsx:15:      setMessage('Missing or invalid token.');
./ms-allis-auth-install/frontend/app/login/page.tsx:28:        setMessage('This link is invalid or expired.');
./ms-allis-auth-install/frontend/app/login/page.tsx:37:        <p className="text-stone-600">{message}</p>
./ms-allis-auth-install/frontend/app/sign-in/page.tsx:23:      setError(err.message || 'Sign in failed');
./ms-allis-auth-install/frontend/lib/api.ts:14:  const res = await fetch(url, {
./ms-allis-auth-install/frontend/lib/api.ts:29:  return jsonFetch<SessionResponse>(`${API_BASE}/api/sign-in`, {
./ms-allis-auth-install/frontend/lib/api.ts:36:  return jsonFetch<SessionResponse>(`${API_BASE}/api/setup-password`, {
./ms-allis-auth-install/frontend/lib/api.ts:43:  return jsonFetch<{ ok: true }>(`${API_BASE}/api/forgot-password`, {
./ms-allis-auth-install/frontend/lib/api.ts:50:  return jsonFetch<{ ueid: string; source: 'approval' | 'reset' }>(`${API_BASE}/api/resolve-token/${encodeURIComponent(token)}`);
./ms-allis-auth-install/frontend/lib/api.ts:54:  return jsonFetch<{ has_password: boolean }>(`${API_BASE}/api/has-password/${encodeURIComponent(ueid)}`);
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./.venv/lib64/python3.12/site-packages/werkzeug/debug/shared/debugger.js:54:      fetch(
./.venv/lib64/python3.12/site-packages/werkzeug/debug/shared/debugger.js:84:    fetch(makeDebugURL({cmd: "printpin"}));
./.venv/lib64/python3.12/site-packages/werkzeug/debug/shared/debugger.js:267:    fetch(makeDebugURL({cmd: command.value, frm: frameID}))
./.venv/lib64/python3.12/site-packages/torch/utils/model_dump/code.js:635:      fetch("./model_info.json").then(function(response) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:5:mpl.get_websocket_type = function () {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:6:    if (typeof WebSocket !== 'undefined') {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:7:        return WebSocket;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:8:    } else if (typeof MozWebSocket !== 'undefined') {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:9:        return MozWebSocket;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:12:            'Your browser does not have WebSocket support. ' +
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:15:                'have to enable WebSockets in about:config.'
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:20:mpl.figure = function (figure_id, websocket, ondownload, parent_element) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:23:    this.ws = websocket;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:32:                'This browser does not support binary websocket messages. ' +
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:40:    this.message = undefined;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:63:        fig.send_message('supports_binary', { value: fig.supports_binary });
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:64:        fig.send_message('send_image_mode', {});
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:66:            fig.send_message('set_device_pixel_ratio', {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:70:        fig.send_message('refresh', {});
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:87:    this.ws.onmessage = this._make_on_message_function(this);
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:195:        // There's no need to resize if the WebSocket is not connected:
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:420:    status_bar.classList = 'mpl-message';
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:422:    this.message = status_bar;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:428:    this.send_message('resize', { width: x_pixels, height: y_pixels });
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:431:mpl.figure.prototype.send_message = function (type, properties) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:437:mpl.figure.prototype.send_draw_message = function () {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:454:        fig.send_message('refresh', {});
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:491:mpl.figure.prototype.handle_message = function (fig, msg) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:492:    fig.message.textContent = msg['message'];
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:497:    fig.send_draw_message();
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:529:    this.send_message('ack', {});
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:532:// A function to construct a web socket function for onmessage handling.
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:534:mpl.figure.prototype._make_on_message_function = function (fig) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:535:    return function socket_on_message(evt) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:542:                 * to be part of the websocket stream */
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:573:        // the figure and JSON message as its only arguments.
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:578:                "No handler for the '%s' message type: ",
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:587:                // console.log("Handling '%s' message: ", msg_type, msg);
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:644:    this.send_message(name, {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:689:    this.send_message(name, { key: value, guiEvent: simpleKeys(event) });
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:697:        this.send_message('toolbar_button', { name: name });
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:702:    this.message.textContent = tooltip;
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:3:var comm_websocket_adapter = function (comm) {
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:4:    // Create a "websocket"-like object which calls the given IPython comm
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:38:        // Pass the mpl event to the overridden (by mpl) onmessage function.
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:39:        ws.onmessage(data);
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:52:    var ws_proxy = comm_websocket_adapter(comm);
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:61:    // web socket which is closed, not our websocket->open comm proxy.
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:97:    fig.send_message('closing', msg);
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:112:    this.send_message('ack', {});
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:178:    status_bar.classList = 'mpl-message pull-right';
./.venv/lib64/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:180:    this.message = status_bar;
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js:54:      fetch(
./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js:84:    fetch(makeDebugURL({cmd: "printpin"}));
./.venv/lib/python3.12/site-packages/werkzeug/debug/shared/debugger.js:267:    fetch(makeDebugURL({cmd: command.value, frm: frameID}))
./.venv/lib/python3.12/site-packages/torch/utils/model_dump/code.js:635:      fetch("./model_info.json").then(function(response) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:5:mpl.get_websocket_type = function () {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:6:    if (typeof WebSocket !== 'undefined') {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:7:        return WebSocket;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:8:    } else if (typeof MozWebSocket !== 'undefined') {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:9:        return MozWebSocket;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:12:            'Your browser does not have WebSocket support. ' +
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:15:                'have to enable WebSockets in about:config.'
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:20:mpl.figure = function (figure_id, websocket, ondownload, parent_element) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:23:    this.ws = websocket;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:32:                'This browser does not support binary websocket messages. ' +
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:40:    this.message = undefined;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:63:        fig.send_message('supports_binary', { value: fig.supports_binary });
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:64:        fig.send_message('send_image_mode', {});
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:66:            fig.send_message('set_device_pixel_ratio', {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:70:        fig.send_message('refresh', {});
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:87:    this.ws.onmessage = this._make_on_message_function(this);
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:195:        // There's no need to resize if the WebSocket is not connected:
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:420:    status_bar.classList = 'mpl-message';
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:422:    this.message = status_bar;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:428:    this.send_message('resize', { width: x_pixels, height: y_pixels });
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:431:mpl.figure.prototype.send_message = function (type, properties) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:437:mpl.figure.prototype.send_draw_message = function () {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:454:        fig.send_message('refresh', {});
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:491:mpl.figure.prototype.handle_message = function (fig, msg) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:492:    fig.message.textContent = msg['message'];
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:497:    fig.send_draw_message();
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:529:    this.send_message('ack', {});
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:532:// A function to construct a web socket function for onmessage handling.
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:534:mpl.figure.prototype._make_on_message_function = function (fig) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:535:    return function socket_on_message(evt) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:542:                 * to be part of the websocket stream */
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:573:        // the figure and JSON message as its only arguments.
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:578:                "No handler for the '%s' message type: ",
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:587:                // console.log("Handling '%s' message: ", msg_type, msg);
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:644:    this.send_message(name, {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:689:    this.send_message(name, { key: value, guiEvent: simpleKeys(event) });
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:697:        this.send_message('toolbar_button', { name: name });
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/mpl.js:702:    this.message.textContent = tooltip;
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:3:var comm_websocket_adapter = function (comm) {
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:4:    // Create a "websocket"-like object which calls the given IPython comm
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:38:        // Pass the mpl event to the overridden (by mpl) onmessage function.
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:39:        ws.onmessage(data);
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:52:    var ws_proxy = comm_websocket_adapter(comm);
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:61:    // web socket which is closed, not our websocket->open comm proxy.
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:97:    fig.send_message('closing', msg);
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:112:    this.send_message('ack', {});
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:178:    status_bar.classList = 'mpl-message pull-right';
./.venv/lib/python3.12/site-packages/matplotlib/backends/web_backend/js/nbagg_mpl.js:180:    this.message = status_bar;
./services/query_enhancer.js:6:function detectQueryType(message) {
./services/query_enhancer.js:7:    const msg = message.toLowerCase();
./services/query_enhancer.js:44:function generateContextualResponse(queryType, message, userId) {
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/chroma_inspect_venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/chroma_inspect_venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/app.js:27:app.post('/chat-with-mountainshares-brain', async (req, res) => {
./services/app.js:28:  const message = req.body.message || '';
./services/app.js:30:  const result = await brain.converse(message, userId);
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/.venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/.venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/ms_jarvis_geographic_research.js:21:  async analyze(message) {
./services/ms_jarvis_geographic_research.js:22:    const msg = message.toLowerCase();
./services/ms_jarvis_geographic_research.js:40:        geoData = await this.processGeographicRequest(message);
./services/ms_jarvis_geographic_research.js:41:        reply = this.generateLocationResponse(geoData, message);
./services/ms_jarvis_geographic_research.js:58:  async processGeographicRequest(message) {
./services/ms_jarvis_geographic_research.js:59:    // Extract potential addresses or coordinates from message
./services/ms_jarvis_geographic_research.js:60:    const addressMatch = message.match(/([A-Za-z\s,]+(?:WV|West Virginia)[^.!?]*)/i);
./services/ms_jarvis_geographic_research.js:92:  generateLocationResponse(geoData, originalMessage) {
./services/ms_jarvis_geographic_research.js:113:  async collaborateWithBrain(brainAgents, message) {
./services/ms_jarvis_geographic_research.js:114:    const geoResult = await this.analyze(message);
./services/ms_jarvis_geographic_research.js:120:        const technicalGeo = await brainAgents.technical.analyze(`geodetic analysis: ${message}`);
./services/ms_jarvis_geographic_research.js:126:        const creativeGeo = await brainAgents.creative.analyze(`mapping visualization: ${message}`);
./services/ms_jarvis_geographic_research.js:135:module.exports = { analyze: async (message) => {
./services/ms_jarvis_geographic_research.js:137:  return agent.analyze(message);
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/venv/lib64/python3.12/site-packages/torch/utils/model_dump/code.js:635:      fetch("./model_info.json").then(function(response) {
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./services/venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./services/venv/lib/python3.12/site-packages/torch/utils/model_dump/code.js:635:      fetch("./model_info.json").then(function(response) {
./services/server.js:27:      message: 'Ms. Jarvis quantum-resistant AGI system operational',
./services/server.js:39:  // Chat endpoint
./services/server.js:40:  if (pathname === '/chat' && req.method === 'POST') {
./services/server.js:49:        const userMessage = data.messages ? data.messages[0]?.content : data.message || 'Hello';
./services/server.js:52:          response: `🤖 Ms. Jarvis: I processed your message "${userMessage}". I am your quantum-resistant AI assistant running locally with advanced security protocols! My private AGI systems remain secure in Mount Hope, WV while providing you safe, filtered interactions.`,
./services/server.js:64:        res.end(JSON.stringify({ error: error.message }));
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./crypto-venv/lib64/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./crypto-venv/lib64/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./crypto-venv/lib/python3.12/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:12:self.addEventListener("message", async function (event) {
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:41:        let errorBytes = encoder.encode(error.message);
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:70:      const response = await fetch(event.data.url, event.data.fetchParams);
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:97:      // all fetching after this goes through a new postmessage call with getMore
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:101:      let errorBytes = encoder.encode(error.message);
./crypto-venv/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/emscripten/emscripten_fetch_worker.js:110:self.postMessage({ inited: true });
./ms-allis-frontend/app/apply/page.tsx:5:import { MsAllisPortrait } from "@/components/MsAllisPortrait";
./ms-allis-frontend/app/apply/page.tsx:73:  async function handleSubmit(e: React.FormEvent) {
./ms-allis-frontend/app/apply/page.tsx:110:      const message =
./ms-allis-frontend/app/apply/page.tsx:114:            ? err.message
./ms-allis-frontend/app/apply/page.tsx:116:      setError(message);
./ms-allis-frontend/app/apply/page.tsx:130:            <MsAllisPortrait size="small" withFrame={false} className="w-10 h-10 rounded-full" />
./ms-allis-frontend/app/apply/page.tsx:132:              Ms. Allis
./ms-allis-frontend/app/apply/page.tsx:154:        <form onSubmit={handleSubmit} className="space-y-10 animate-fade-in-up" style={{ animationDelay: "0.15s" }}>
./ms-allis-frontend/app/apply/page.tsx:418:          {/* Error message */}
./ms-allis-frontend/app/apply/page.tsx:458:          <MsAllisPortrait size="medium" withFrame className="mb-10" />
./ms-allis-frontend/app/portal/page.tsx:15:import { ChatPanel } from "@/components/ChatPanel";
./ms-allis-frontend/app/portal/page.tsx:17:import { MsAllisPortrait } from "@/components/MsAllisPortrait";
./ms-allis-frontend/app/portal/page.tsx:31:  message_count: number;
./ms-allis-frontend/app/portal/page.tsx:238:            <MsAllisPortrait size="small" withFrame={false} className="w-24 h-24" />
./ms-allis-frontend/app/portal/page.tsx:240:              <p className="font-display text-base text-teal-deep">Ms. Allis</p>
./ms-allis-frontend/app/portal/page.tsx:322:  const [showChat, setShowChat] = useState(false);
./ms-allis-frontend/app/portal/page.tsx:343:    fetch(`/api/conversation/threads${uid}`)
./ms-allis-frontend/app/portal/page.tsx:356:    await fetch("/api/conversation/threads", {
./ms-allis-frontend/app/portal/page.tsx:367:    await fetch("/api/conversation/threads", {
./ms-allis-frontend/app/portal/page.tsx:478:          onClick={() => setShowChat((v) => !v)}
./ms-allis-frontend/app/portal/page.tsx:481:          {showChat ? "Hide Ms. Allis" : "Talk to Ms. Allis →"}
./ms-allis-frontend/app/portal/page.tsx:491:      {/* Chat panel — toggles open/closed */}
./ms-allis-frontend/app/portal/page.tsx:492:      {showChat && (
./ms-allis-frontend/app/portal/page.tsx:506:                  title="Start a new conversation with Ms. Allis"
./ms-allis-frontend/app/portal/page.tsx:533:                      Your conversations with Ms. Allis will appear here.
./ms-allis-frontend/app/portal/page.tsx:651:                                      {t.message_count > 0 ? ` · ${t.message_count} msg${t.message_count !== 1 ? "s" : ""}` : ""}
./ms-allis-frontend/app/portal/page.tsx:727:            {/* ──── Chat area ──── */}
./ms-allis-frontend/app/portal/page.tsx:729:              <ChatPanel
./ms-allis-frontend/app/page.tsx:2:import { MsAllisPortrait } from "@/components/MsAllisPortrait";
./ms-allis-frontend/app/page.tsx:26:              <MsAllisPortrait size="hero" withFrame />
./ms-allis-frontend/app/page.tsx:40:                Ms. Allis<span className="text-terracotta">.</span>
./ms-allis-frontend/app/page.tsx:86:      {/* === WHO IS MS. ALLIS === */}
./ms-allis-frontend/app/page.tsx:91:              Who is Ms. Allis?
./ms-allis-frontend/app/page.tsx:104:                Ms. Allis is grounded in West Virginia — every belief she holds is
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && sed -n '1,260p' ms_jarvis_unified_gateway.py

# --- WV entangled /chat_wv proxy ---
import httpx
from pydantic import BaseModel as _WVBaseModel

class _WVChatPayload(_WVBaseModel):
    message: str
    user_id: str | None = None

@app.post("/chat_wv")
async def chat_wv_proxy(payload: _WVChatPayload):
    """
    Proxy WV‑entangled chat to jarvis-wv-entangled-gateway.
    This keeps unified gateway thin while exposing the entangled path on 8001.
    """
    async with httpx.AsyncClient(timeout=600.0) as client:
        resp = await client.post(
            "http://jarvis-wv-entangled-gateway:8010/chat_wv",
            json={"message": payload.message, "user_id": payload.user_id},
        )
        resp.raise_for_status()
        return resp.json()
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && sed -n '1,260p' ms-allis-auth-install/backend/auth_api_patch.py
# Patch content for /app/services/auth_api.py
# Apply manually or via install script.

import hashlib
import json
import logging
import os
import secrets
import sys
from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
import redis
from fastapi import FastAPI, Header, HTTPException, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

sys.path.insert(0, os.path.dirname(__file__))
from wallet_service import WalletService, WalletAlreadyExistsError
from registration_pipeline import write_immutable_record

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("auth_api")

REDIS_URL       = os.getenv("REDIS_URL", "redis://jarvis-redis:6379")
ADMIN_API_KEY   = os.getenv("JARVIS_API_KEY", "super-secret-key")
RESEND_API_KEY  = os.getenv("RESEND_API_KEY", "")
MAGIC_LINK_BASE = os.getenv("MAGIC_LINK_BASE_URL", "http://localhost:3000")
MAGIC_LINK_TTL  = int(os.getenv("MAGIC_LINK_TTL_SECONDS", 900))
PASSWORD_RESET_TTL = int(os.getenv("PASSWORD_RESET_TTL_SECONDS", 900))
SESSION_TTL = int(os.getenv("SESSION_TTL_SECONDS", 60 * 60 * 24 * 30))
BCRYPT_ROUNDS = int(os.getenv("BCRYPT_ROUNDS", 12))

WV_COUNTIES = [
    "Barbour","Berkeley","Boone","Braxton","Brooke","Cabell","Calhoun","Clay",
    "Doddridge","Fayette","Gilmer","Grant","Greenbrier","Hampshire","Hancock",
    "Hardy","Harrison","Jackson","Jefferson","Kanawha","Lewis","Lincoln","Logan",
    "Marion","Marshall","Mason","McDowell","Mercer","Mineral","Mingo","Monongalia",
    "Monroe","Morgan","Nicholas","Ohio","Pendleton","Pleasants","Pocahontas",
    "Preston","Putnam","Raleigh","Randolph","Ritchie","Roane","Summers","Taylor",
    "Tucker","Tyler","Upshur","Wayne","Webster","Wetzel","Wirt","Wood","Wyoming"
]

app = FastAPI(title="Ms. Allis Auth API", version="1.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://allis.mountainshares.us", "https://mountainshares.us", "http://localhost:3000", os.getenv("FRONTEND_URL", "")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

r = redis.from_url(REDIS_URL, decode_responses=True)
wallet_svc = WalletService(redis_client=redis.from_url(REDIS_URL))

def _require_admin(x_api_key: str = Header(...)):
    if x_api_key != ADMIN_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

def _require_session(x_session_token: str = Header(...)) -> dict:
    raw = r.get(f"session:{x_session_token}")
    if not raw:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    return json.loads(raw)

def _generate_ueid(email: str, dl_b64: str) -> str:
    dl_hash = hashlib.sha256(dl_b64.encode()).hexdigest()
    combined = f"{email.lower()}:{dl_hash}"
    return "UEID-" + hashlib.sha256(combined.encode()).hexdigest()[:16].upper()

def _email_hash(email: str) -> str:
    return hashlib.sha256(email.strip().lower().encode()).hexdigest()

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def _new_token(n: int = 32) -> str:
    return secrets.token_urlsafe(n)

def _hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=BCRYPT_ROUNDS)).decode()

def _check_password(password: str, pw_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode(), pw_hash.encode())
    except Exception:
        return False

def _create_session(ueid: str, email: str, name: str) -> dict:
    token = _new_token()
    payload = {
        "ueid": ueid,
        "email": email,
        "name": name,
        "created_at": _now_iso(),
    }
    r.set(f"session:{token}", json.dumps(payload), ex=SESSION_TTL)
    return {"session_token": token, "user": payload}

def _send_apply_confirmation(email: str, name: str):
    try:
        import httpx
        resp = httpx.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
            json={
                "from": "Ms. Allis <ms.allis@mountainshares.us>",
                "to": [email],
                "subject": "We received your Community Champion application",
                "html": f"""
                <p>Hi {name},</p>
                <p>We received your Community Champion application and Carrie will review it soon.</p>
                <p>If approved, you'll receive a separate email with a link to set your password and sign in.</p>
                <p>No action is needed right now.</p>
                """,
            },
            timeout=10,
        )
        resp.raise_for_status()
        log.info(f"[APPLY-CONFIRM] sent to {email}")
    except Exception as exc:
        log.error(f"[APPLY-CONFIRM] send failed for {email}: {exc}")

def _send_setup_password_email(email: str, token: str, name: str):
    url = f"{MAGIC_LINK_BASE}/setup-password?token={token}"
    try:
        import httpx
        resp = httpx.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
            json={
                "from": "Ms. Allis <ms.allis@mountainshares.us>",
                "to": [email],
                "subject": "Set your password and sign in",
                "html": f"""
                <p>Hi {name},</p>
                <p>Your Community Champion application was approved.</p>
                <p>Click below to set your password and sign in. This link expires in 15 minutes.</p>
                <p><a href=\"{url}\">{url}</a></p>
                <p>If you didn't request this, ignore it.</p>
                """,
            },
            timeout=10,
        )
        resp.raise_for_status()
        log.info(f"[SETUP] sent to {email}")
    except Exception as exc:
        log.error(f"[SETUP] send failed for {email}: {exc}")

def _send_password_reset_email(email: str, token: str, name: str = "there"):
    url = f"{MAGIC_LINK_BASE}/login?token={token}"
    try:
        import httpx
        resp = httpx.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
            json={
                "from": "Ms. Allis <ms.allis@mountainshares.us>",
                "to": [email],
                "subject": "Reset your password",
                "html": f"""
                <p>Hi {name},</p>
                <p>We received a request to reset your password.</p>
                <p>Click below to continue. This link expires in 15 minutes.</p>
                <p><a href=\"{url}\">{url}</a></p>
                <p>If you didn't request this, ignore it.</p>
                """,
            },
            timeout=10,
        )
        resp.raise_for_status()
        log.info(f"[RESET] sent to {email}")
    except Exception as exc:
        log.error(f"[RESET] send failed for {email}: {exc}")

class SetupPasswordBody(BaseModel):
    token: str
    password: str

class SignInBody(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordBody(BaseModel):
    email: EmailStr

# Existing routes remain above/below; patch these behaviors into current file:
# - In /api/apply, call _send_apply_confirmation(email, name) before return.
# - In /api/approve/{ueid}, replace magic email sender with _send_setup_password_email(...).
# - Add endpoints below.

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/resolve-token/{token}")
async def resolve_token(token: str):
    raw = r.get(f"magic:{token}")
    if raw:
        data = json.loads(raw)
        return {"ueid": data["ueid"], "source": "approval"}
    raw = r.get(f"password_reset:{token}")
    if raw:
        data = json.loads(raw)
        return {"ueid": data["ueid"], "source": "reset"}
    raise HTTPException(400, "Invalid or expired token.")

@app.get("/api/has-password/{ueid}")
async def has_password(ueid: str):
    return {"has_password": bool(r.exists(f"password:{ueid}"))}

@app.post("/api/setup-password")
async def setup_password(body: SetupPasswordBody):
    if len(body.password) < 10:
        raise HTTPException(400, "Password must be at least 10 characters.")

    source = None
    payload = None
    raw = r.get(f"magic:{body.token}")
    if raw:
        source = "magic"
        payload = json.loads(raw)
    else:
        raw = r.get(f"password_reset:{body.token}")
        if raw:
            source = "password_reset"
            payload = json.loads(raw)

    if not payload:
        raise HTTPException(400, "Invalid or expired token.")

    ueid = payload["ueid"]
    existing = r.hgetall(f"password:{ueid}")
    created_at = existing.get("created_at") or _now_iso()
    r.hset(f"password:{ueid}", mapping={
        "hash": _hash_password(body.password),
        "created_at": created_at,
        "updated_at": _now_iso(),
    })

    session = _create_session(
        ueid=ueid,
        email=payload.get("email", ""),
        name=payload.get("name", ""),
    )

    if source == "magic":
        r.delete(f"magic:{body.token}")
    else:
        r.delete(f"password_reset:{body.token}")

    return session

@app.post("/api/sign-in")
async def sign_in(body: SignInBody):
    email_key = f"applicant:email:{_email_hash(body.email)}"
    ueid = r.get(email_key)
    if not ueid:
        raise HTTPException(401, "Invalid email or password.")
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && sed -n '1,260p' ms-allis-auth-install/backend/registration_pipeline.py
"""
registration_pipeline.py
Orchestrates the full registration flow before user hash creation.
MVP: DL OCR + expiry check + UEID + immutable SQLite write
Face match: deferred to v2
"""
import os, re, uuid, hashlib, base64, sqlite3, logging
from datetime import datetime
from typing import Tuple

logger = logging.getLogger("registration_pipeline")

DB_PATH = os.getenv("GISGEODB_PATH", "data/GISGEODB_ACTIVE.sqlite")


# ── 1. DL OCR + expiry ───────────────────────────────────────────────────────

def validate_dl_image(dl_image_b64: str) -> Tuple[bool, str, dict]:
    """
    Returns (passed, message, extracted_data)
    extracted_data keys: full_name, expiration_date, expires_in_days
    """
    if not dl_image_b64:
        return False, "No driver's license image provided", {}

    try:
        import pytesseract
        from PIL import Image
        import io

        raw = dl_image_b64.split(",")[1] if "," in dl_image_b64 else dl_image_b64
        img_bytes = base64.b64decode(raw)
        img = Image.open(io.BytesIO(img_bytes))
        text = pytesseract.image_to_string(img)

        data = _parse_wv_dl(text)

        if data.get("is_expired"):
            return False, f"Driver's license expired: {data.get('expiration_date')}", data

        if not data.get("expiration_date"):
            # Warn but don't block — OCR can miss subscript formatting
            logger.warning("[DL] Could not parse expiration date from DL image")

        return True, data.get("verification_message", "DL valid"), data

    except ImportError:
        logger.warning("[DL] pytesseract not available — skipping OCR validation")
        return True, "OCR unavailable — DL accepted", {}
    except Exception as exc:
        logger.error(f"[DL] OCR error: {exc}")
        return False, f"DL validation error: {exc}", {}


def _parse_wv_dl(text: str) -> dict:
    """Parse WV DL text — handles subscript 4b + Exp MM/DD/YYYY format"""
    result = {
        "raw_text": text,
        "full_name": None,
        "expiration_date": None,
        "is_expired": False,
        "expires_in_days": None,
        "verification_message": "",
    }

    # Expiration — WV format: Exp MM/DD/YYYY (subscript 4b may appear before it)
    match = re.search(r'[Ee]xp[\s:.]+(\d{2}[/-]\d{2}[/-]\d{4})', text)
    if match:
        exp_str = match.group(1).replace("-", "/")
        result["expiration_date"] = exp_str
        try:
            exp_date = datetime.strptime(exp_str, "%m/%d/%Y")
            days = (exp_date - datetime.now()).days
            result["expires_in_days"] = days
            if days < -30:
                result["is_expired"] = True
                result["verification_message"] = f"REJECTED: Expired {abs(days)} days ago"
            elif days < 0:
                result["verification_message"] = f"GRACE PERIOD: {30+days} days remaining"
            elif days <= 30:
                result["verification_message"] = f"WARNING: Expires in {days} days"
            else:
                result["verification_message"] = f"VALID: Expires in {days} days"
        except ValueError:
            result["verification_message"] = "Could not parse expiration date"

    # Name — WV DL usually has LN, FN MI format
    name_match = re.search(r'([A-Z]{2,}),\s*([A-Z]{2,})', text)
    if name_match:
        result["full_name"] = f"{name_match.group(2)} {name_match.group(1)}"

    return result


# ── 2. Generate private UEID (immutable, never exposed in API responses) ─────

def generate_ueid() -> str:
    """MS-JARVIS-{16 hex chars} — matches legacy format"""
    return f"MS-JARVIS-{uuid.uuid4().hex[:16].upper()}"


# ── 3. Write immutable security layer ────────────────────────────────────────

def write_immutable_record(
    ueid: str,
    dl_image_b64: str,
    wallet_address: str,
    wallet_private_key_encrypted: str,
    email: str,
    selfie_image_b64: str = "",
) -> bool:
    """
    Write-once row to ueid_immutable_security (v2 schema).
    Core identity fields are immutable; supersession fields are mutable
    only via authorized supersession events.
    """
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Ensure table + triggers exist (matches create_immutable_security_layer.py)
        c.executescript("""
            CREATE TABLE IF NOT EXISTS ueid_immutable_security (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ueid TEXT UNIQUE NOT NULL,
                driver_license_hash TEXT NOT NULL,
                email_hash TEXT NOT NULL DEFAULT '',
                selfie_hash TEXT NOT NULL DEFAULT '',
                wallet_address TEXT UNIQUE NOT NULL,
                wallet_private_key_encrypted TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                locked INTEGER DEFAULT 1,
                status TEXT NOT NULL DEFAULT 'active',
                superseded_by TEXT,
                superseded_at DATETIME,
                superseded_by_admin TEXT,
                supersession_reason TEXT,
                court_case_number TEXT,
                court_doc_ref TEXT,
                legal_hold_until DATETIME
            );

            CREATE TABLE IF NOT EXISTS ueid_immutable_access_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ueid TEXT NOT NULL,
                action TEXT,
                accessed_by TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                access_result TEXT
            );

            CREATE TABLE IF NOT EXISTS ueid_supersession_audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_ueid TEXT NOT NULL,
                new_ueid TEXT NOT NULL,
                status_before TEXT,
                status_after TEXT,
                admin_userid TEXT NOT NULL,
                court_case_number TEXT,
                reason TEXT NOT NULL,
                court_doc_redis_key TEXT,
                ip_address TEXT,
                ts DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

        dl_hash = hashlib.sha256(dl_image_b64.encode()).hexdigest()
        email_hash = hashlib.sha256(email.lower().encode()).hexdigest()
        selfie_hash = hashlib.sha256(selfie_image_b64.encode()).hexdigest() if selfie_image_b64 else ""

        c.execute(
            """INSERT INTO ueid_immutable_security
               (ueid, driver_license_hash, email_hash, selfie_hash,
                wallet_address, wallet_private_key_encrypted, status)
               VALUES (?, ?, ?, ?, ?, ?, 'active')""",
            (ueid, dl_hash, email_hash, selfie_hash, wallet_address, wallet_private_key_encrypted),
        )
        c.execute(
            "INSERT INTO ueid_immutable_access_log (ueid, action) VALUES (?, ?)",
            (ueid, "created"),
        )
        conn.commit()
        conn.close()
        logger.info(f"[UEID] Immutable record written: {ueid}")
        return True

    except sqlite3.IntegrityError as exc:
        logger.error(f"[UEID] Duplicate or integrity error: {exc}")
        return False
    except Exception as exc:
        logger.error(f"[UEID] Write failed: {exc}")
        return False


def supersede_immutable_record(
    original_ueid: str,
    new_ueid: str,
    admin_userid: str,
    reason: str,
    court_case_number: str = "",
    court_doc_redis_key: str = "",
    ip_address: str = "",
) -> bool:
    """
    Mark an existing UEID as superseded by a new one. The new UEID's row
    must already exist (created via the normal apply flow before this is called).
    Logs the rotation to ueid_supersession_audit.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Verify both rows exist
        c.execute("SELECT status FROM ueid_immutable_security WHERE ueid = ?", (original_ueid,))
        old_row = c.fetchone()
        if not old_row:
            logger.error(f"[SUPERSEDE] original UEID not found: {original_ueid}")
            return False
        if old_row[0] != "active":
            logger.error(f"[SUPERSEDE] original UEID not active (status={old_row[0]}): {original_ueid}")
            return False

        c.execute("SELECT 1 FROM ueid_immutable_security WHERE ueid = ?", (new_ueid,))
        if not c.fetchone():
            logger.error(f"[SUPERSEDE] new UEID not found: {new_ueid}")
            return False

        # Update old row's supersession columns (allowed by trigger)
        from datetime import datetime, timezone
        now_iso = datetime.now(timezone.utc).isoformat()
        c.execute("""
            UPDATE ueid_immutable_security
            SET status = 'superseded',
                superseded_by = ?,
                superseded_at = ?,
                superseded_by_admin = ?,
                supersession_reason = ?,
                court_case_number = ?,
                court_doc_ref = ?
            WHERE ueid = ?
        """, (new_ueid, now_iso, admin_userid, reason, court_case_number, court_doc_redis_key, original_ueid))

        # Append audit row
        c.execute("""
            INSERT INTO ueid_supersession_audit
            (original_ueid, new_ueid, status_before, status_after,
             admin_userid, court_case_number, reason, court_doc_redis_key, ip_address)
            VALUES (?, ?, 'active', 'superseded', ?, ?, ?, ?, ?)
        """, (original_ueid, new_ueid, admin_userid, court_case_number,
              reason, court_doc_redis_key, ip_address))

        # Append access log entries for both UEIDs
        c.execute("INSERT INTO ueid_immutable_access_log (ueid, action, accessed_by) VALUES (?, ?, ?)",
                  (original_ueid, "superseded", admin_userid))
        c.execute("INSERT INTO ueid_immutable_access_log (ueid, action, accessed_by) VALUES (?, ?, ?)",
                  (new_ueid, "supersedes_" + original_ueid, admin_userid))

        conn.commit()
        conn.close()
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ cd /opt/msjarvis-rebuild && sed -n '1,260p' ms-allis-auth-install/backend/wallet_service.py
"""
wallet_service.py — MountainShares custodial wallet management

Generates a real Ethereum keypair per user. The public address is stored in plaintext.
The private key is encrypted with Fernet (AES-128 + HMAC) using a master key, then stored
in Redis. Master key lives in ~/.msallis/wallet_master.key (chmod 600), with override via
the MSALLIS_WALLET_MASTER_KEY environment variable for production deployments.

Storage shape:
    wallet:<userid> = hash {
        address:           "0x...",            # public Eth address
        encrypted_privkey: "<fernet token>",   # encrypted with master key
        created_at:        "<iso8601 utc>",
        custodial:         "true" | "false",   # str — Redis stores strings
        chain:             "arbitrum-one"      # default; can change per-deployment
    }

Future graduation flow (not in v1): expose export_and_revoke(userid) which decrypts the
private key, returns it once to the user, and deletes the server copy.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from cryptography.fernet import Fernet, InvalidToken
from eth_account import Account


# Enable HD wallet features for mnemonic support if we ever want them later.
Account.enable_unaudited_hdwallet_features()


class WalletError(Exception):
    """Base class for wallet errors."""


class WalletAlreadyExistsError(WalletError):
    pass


class WalletNotFoundError(WalletError):
    pass


class WalletService:
    """
    Manages custodial Ethereum wallets for Ms. Allis users.

    The master encryption key is loaded once at construction time. The same key must be
    used for every encrypt/decrypt cycle of a given user's private key — losing the
    master key means losing access to every user's funds. Back this up offline.
    """

    DEFAULT_MASTER_KEY_PATH = Path.home() / ".msallis" / "wallet_master.key"
    DEFAULT_CHAIN = "arbitrum-one"

    def __init__(self, redis_client, master_key: Optional[bytes] = None,
                 master_key_path: Optional[Path] = None,
                 chain: str = DEFAULT_CHAIN):
        self.redis = redis_client
        self.chain = chain
        self._fernet = Fernet(master_key or self._load_or_create_master_key(master_key_path))

    @staticmethod
    def _load_or_create_master_key(path: Optional[Path]) -> bytes:
        # Env var wins — preferred for production.
        env_key = os.getenv("MSALLIS_WALLET_MASTER_KEY")
        if env_key:
            return env_key.encode() if isinstance(env_key, str) else env_key

        key_path = path or WalletService.DEFAULT_MASTER_KEY_PATH
        if key_path.exists():
            return key_path.read_bytes().strip()

        # First run — generate and persist with locked-down permissions.
        key_path.parent.mkdir(parents=True, exist_ok=True)
        new_key = Fernet.generate_key()
        key_path.write_bytes(new_key)
        os.chmod(key_path, 0o600)
        return new_key

    def _wallet_key(self, userid: str) -> str:
        return f"wallet:{userid}"

    def create_wallet(self, userid: str) -> dict:
        """
        Generates a fresh keypair, stores encrypted record, returns public-safe metadata.
        Raises WalletAlreadyExistsError if a wallet already exists for this userid.
        """
        key = self._wallet_key(userid)
        if self.redis.exists(key):
            raise WalletAlreadyExistsError(f"wallet already exists for {userid}")

        acct = Account.create()
        privkey_hex = acct.key.hex()
        encrypted = self._fernet.encrypt(privkey_hex.encode()).decode()

        record = {
            "address": acct.address,
            "encrypted_privkey": encrypted,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "custodial": "true",
            "chain": self.chain,
        }
        self.redis.hset(key, mapping=record)

        return {
            "userid": userid,
            "address": acct.address,
            "chain": self.chain,
            "custodial": True,
            "created_at": record["created_at"],
        }

    def get_wallet_public(self, userid: str) -> dict:
        """Returns public-safe wallet info — never the private key."""
        record = self.redis.hgetall(self._wallet_key(userid))
        if not record:
            raise WalletNotFoundError(f"no wallet for {userid}")
        record = _decode(record)
        return {
            "userid": userid,
            "address": record["address"],
            "chain": record.get("chain", self.chain),
            "custodial": record.get("custodial", "true") == "true",
            "created_at": record["created_at"],
        }

    def reveal_private_key(self, userid: str, reason: str) -> str:
        """
        Decrypts and returns the user's private key. AUDIT-LOGGED.

        Use only for: (1) export_and_revoke graduation flow, (2) explicit user-requested
        recovery, (3) admin emergency. The `reason` arg is required and gets logged so
        every reveal has a paper trail.
        """
        if not reason or not reason.strip():
            raise ValueError("reason is required for reveal_private_key")

        record = self.redis.hgetall(self._wallet_key(userid))
        if not record:
            raise WalletNotFoundError(f"no wallet for {userid}")
        record = _decode(record)

        try:
            privkey = self._fernet.decrypt(record["encrypted_privkey"].encode()).decode()
        except InvalidToken as e:
            raise WalletError("master key cannot decrypt this wallet — wrong key?") from e

        # Audit log entry — append to a Redis list per-user.
        audit_entry = json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(),
            "reason": reason,
        })
        self.redis.rpush(f"wallet:audit:{userid}", audit_entry)

        return privkey


def _decode(redis_hash: dict) -> dict:
    """fakeredis returns str, real redis returns bytes — normalize to str."""
    out = {}
    for k, v in redis_hash.items():
        k = k.decode() if isinstance(k, bytes) else k
        v = v.decode() if isinstance(v, bytes) else v
        out[k] = v
    return out
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/opt/msjarvis-rebuild$ 

