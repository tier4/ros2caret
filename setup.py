from __future__ import annotations

from setuptools import find_packages, setup


package_name = 'ros2caret'

setup(
    name=package_name,
    version='0.6.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['ros2cli'],
    zip_safe=True,
    maintainer='ymski, isp-uetsuki',
    maintainer_email='yamasaki@isp.co.jp, uetsuki@isp.co.jp',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'caret = ros2caret.command.caret:CaretCommand',
        ],
        'ros2cli.extension_point': [
            'ros2caret.verb = ros2caret.verb:VerbExtension'
        ],
        'ros2caret.verb': [
            'check_caret_rclcpp = \
                    ros2caret.verb.check_caret_rclcpp:CheckCaretRclcppVerb',
            'check_ctf = ros2caret.verb.check_ctf:CheckCTFVerb',
            'trace_point_summary = \
                    ros2caret.verb.trace_point_summary:TracePointSummaryVerb',
            'topic_summary = ros2caret.verb.topic_summary:TopicSummaryVerb',
            'node_summary = ros2caret.verb.node_summary:NodeSummaryVerb',
            'create_architecture_file = \
                    ros2caret.verb.create_architecture:CreateArchitectureVerb',
            'verify_paths = \
                    ros2caret.verb.verify_paths:VerifyPathsVerb',
            'record = \
                    ros2caret.verb.record:RecordVerb',
            'version = \
                    ros2caret.verb.version:CaretVersionVerb',
        ]
    },
)
