import xml.etree.ElementTree as ET

# Membuat root elemen
root = ET.Element("process", version="9.10.011")

# Membuat elemen context
context = ET.SubElement(root, "context")
ET.SubElement(context, "input")
ET.SubElement(context, "output")
ET.SubElement(context, "macros")

# Membuat elemen operator
operator = ET.SubElement(root, "operator", activated="true", class="process", compatibility="9.10.011", expanded="true", name="Process")
ET.SubElement(operator, "parameter", key="logverbosity", value="init")
ET.SubElement(operator, "parameter", key="random_seed", value="2001")
ET.SubElement(operator, "parameter", key="send_mail", value="never")
ET.SubElement(operator, "parameter", key="notification_email", value="")
ET.SubElement(operator, "parameter", key="process_duration_for_mail", value="30")
ET.SubElement(operator, "parameter", key="encoding", value="SYSTEM")

# Membuat elemen process di dalam operator
process = ET.SubElement(operator, "process", expanded="true")

# Elemen retrieve
retrieve = ET.SubElement(process, "operator", activated="true", class="retrieve", compatibility="9.10.011", expanded="true", height="68", name="Retrieve data_blt_numerik", width="90", x="246", y="34")
ET.SubElement(retrieve, "parameter", key="repository_entry", value="data_blt_numerik")

# Elemen cross_validation
cross_validation = ET.SubElement(process, "operator", activated="true", class="concurrency:cross_validation", compatibility="9.10.011", expanded="true", height="145", name="Cross Validation", width="90", x="447", y="34")
ET.SubElement(cross_validation, "parameter", key="split_on_batch_attribute", value="false")
ET.SubElement(cross_validation, "parameter", key="leave_one_out", value="false")
ET.SubElement(cross_validation, "parameter", key="number_of_folds", value="10")
ET.SubElement(cross_validation, "parameter", key="sampling_type", value="automatic")
ET.SubElement(cross_validation, "parameter", key="use_local_random_seed", value="false")
ET.SubElement(cross_validation, "parameter", key="local_random_seed", value="1992")
ET.SubElement(cross_validation, "parameter", key="enable_parallel_execution", value="true")

# Elemen neural_net di dalam cross_validation
neural_net = ET.SubElement(cross_validation, "process", expanded="true")
neural_net_operator = ET.SubElement(neural_net, "operator", activated="true", class="neural_net", compatibility="9.10.011", expanded="true", height="82", name="Neural Net", width="90", x="112", y="34")
hidden_layers = ET.SubElement(neural_net_operator, "list", key="hidden_layers")
ET.SubElement(hidden_layers, "parameter", key="layer 1", value="5")
ET.SubElement(neural_net_operator, "parameter", key="training_cycles", value="500")
ET.SubElement(neural_net_operator, "parameter", key="learning_rate", value="0.64")
ET.SubElement(neural_net_operator, "parameter", key="momentum", value="0.37")
ET.SubElement(neural_net_operator, "parameter", key="decay", value="false")
ET.SubElement(neural_net_operator, "parameter", key="shuffle", value="true")
ET.SubElement(neural_net_operator, "parameter", key="normalize", value="true")
ET.SubElement(neural_net
