ARG POLICY=manylinux2014
ARG PLATFORM=x86_64

FROM quay.io/pypa/${POLICY}_${PLATFORM}

ARG USERNAME=vscode
ARG HOME=/home/${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ARG INSTALL_ZSH=false

ARG SCRIPT_DOWNLOAD_LOCATION=/tmp/common-redhat.sh
ADD https://raw.githubusercontent.com/microsoft/vscode-dev-containers/main/script-library/common-redhat.sh ${SCRIPT_DOWNLOAD_LOCATION}

RUN \
    #
    # Run Setup script
    chmod +x ${SCRIPT_DOWNLOAD_LOCATION} \
    && bash -c ${SCRIPT_DOWNLOAD_LOCATION} "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "false" \
    && rm -f ${SCRIPT_DOWNLOAD_LOCATION} \
    #
    # Install dependencies
    && yum -y install \
        subversion \
        libXi-devel \
    #
    # Add directories to cache extensions
    && mkdir -p \
        ${HOME}/.vscode-server \
        ${HOME}/.vscode-server-insiders \
    && chown -R ${USERNAME}:${USERNAME} \
        ${HOME}/.vscode-server \
        ${HOME}/.vscode-server-insiders \
    #
    # Clean up
    && yum clean all \
    && rm -rf /var/cache/yum

USER ${USERNAME}
