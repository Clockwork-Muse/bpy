ARG POLICY
ARG PLATFORM

FROM quay.io/pypa/manylinux2014_x86_64

RUN yum -y install \
        sudo \
        subversion \
    #
    # Clean up
    && yum clean all \
    && rm -rf /var/cache/yum

ARG USERNAME
ARG HOME=/home/${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    #
    # Add sudo support.
    && usermod -aG wheel ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    #
    # Add directories to cache extensions
    && mkdir -p \
        ${HOME}/.vscode-server \
        ${HOME}/.vscode-server-insiders \
    && chown -R ${USERNAME}:${USERNAME} \
        ${HOME}/.vscode-server \
        ${HOME}/.vscode-server-insiders

USER ${USERNAME}
